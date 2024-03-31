#!/bin/bash

# Prereqs
# We use jq in a few commands. Making sure it's installed
wget https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64
chmod +x jq-linux-amd64
mv ./jq-linux-amd64 /usr/local/bin/jq

# Changing directory to the /config directory where the volume is mounted
cd /config
mkdir -p certs
mkdir -p client_pub_keys
mkdir -p host_pub_keys

read -p "Go to $VAULT_URL/ui/ for the setup. Press enter to continue"

VAULT_RETRIES=5
echo "Vault is starting..."
until vault status > /dev/null 2>&1 || [ "$VAULT_RETRIES" -eq 0 ]; do
        echo "Waiting for vault to start...: $((VAULT_RETRIES--))"
        sleep 1
done

echo "Authenticating to vault..."
vault login

#
# Username & Password Auth
#

vault auth enable userpass

echo -n "Insert Ansible account password that will be created: "
read -s password_ansible

vault write auth/userpass/users/ansible \
    password=$password_ansible \
    policies=ansible

echo "Creating ansible policy"
vault policy write ansible /config/ansible-policy.hcl

#
# Entra ID Authentication
#

echo "Enabling Entra ID Authentication"
vault auth enable oidc

vault write auth/oidc/config \
        oidc_discovery_url="$ENTRA_ID_DISCOVERY_URL" \
        oidc_client_id="$ENTRA_ID_CLIENT_ID" \
        oidc_client_secret="$ENTRA_ID_CLIENT_SECRET" \
        default_role="entraid"

vault write auth/oidc/role/entraid \
        user_claim="sub" \
        oidc_scopes="https://graph.microsoft.com/.default profile" \
        policies=default \
        ttl=1h \
        allowed_redirect_uris="http://localhost:8250/oidc/callback" \
        allowed_redirect_uris="https://localhost:8250/oidc/callback" \
        allowed_redirect_uris="$VAULT_URL/ui/vault/auth/oidc/oidc/callback" \
        groups_claim="roles"
        # groups_claim="groups" # Should be commented because I'm in too many groups

echo "Restricting claims to only approved roles"

vault write auth/oidc/role/entraid -<<EOF
{
  "bound_claims": {
        "roles": [
            "admin",
            "user"
        ]
    }
}
EOF

echo "Creating admin policy"
vault policy write admin /config/admin-policy.hcl

echo "Adding external groups"

vault write -format=json identity/group name="admin" \
        policies="admin" \
        type="external"

vault write -format=json identity/group name="user" \
        policies="user" \
        type="external"

echo "Adding aliases"

vault_admin_id=$(vault read identity/group/name/admin --format=json | jq -r ".data.id")
vault_user_id=$(vault read identity/group/name/user --format=json | jq -r ".data.id")
entra_id_accessor=$(vault auth list -format=json | jq -r '.["oidc/"].accessor')

vault write identity/group-alias name="admin" \
     mount_accessor=$entra_id_accessor \
     canonical_id=$vault_admin_id

vault write identity/group-alias name="user" \
     mount_accessor=$entra_id_accessor \
     canonical_id=$vault_user_id

#
# Certificate Services
#

echo "Initializing certificate services"
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

vault secrets enable -path=pki_int pki
vault secrets tune -max-lease-ttl=43800h pki_int

echo "Generating the Root CA"
vault write -field=certificate pki/root/generate/internal \
        common_name="$ROOT_CA_COMMON_NAME" \
        key_bits=4096 \
        ttl=87600h > certs/Root_CA.crt

echo "Configuring the Root CA URLs"
vault write pki/config/urls \
        issuing_certificates="$VAULT_URL/v1/pki/ca" \
        crl_distribution_points="$VAULT_URL/v1/pki/crl"

echo "Generating the Intermediate CA CSR"
vault write -format=json pki_int/intermediate/generate/internal \
        common_name="$INT_CA_COMMON_NAME" \
        key_bits=4096 \
        | jq -r '.data.csr' > certs/Int_CA.csr

echo "Configuring the Intermediate CA URLs"
vault write pki_int/config/urls \
        issuing_certificates="$VAULT_URL/v1/pki_int/ca" \
        crl_distribution_points="$VAULT_URL/v1/pki_int/crl"

echo "Sign the Intermediate CA certificate"
vault write -format=json pki/root/sign-intermediate csr=@certs/Int_CA.csr \
        format=pem_bundle ttl="43800h" \
        | jq -r '.data.certificate' > certs/Int_CA.pem

echo "Import the Intermediate CA back into the vault"
vault write pki_int/intermediate/set-signed certificate=@certs/Int_CA.pem

echo "Create the server certificate role for $DOMAINNAME"
vault write pki_int/roles/$VAULT_ENTRA_ID_ROLE_NAME \
        allowed_domains="$DOMAINNAME" \
        allow_localhost=false \
        allow_subdomains=true \
        key_type=rsa \
        key_bits=4096 \
        max_ttl="17531h"

echo "Create the legacy server certificate role for $DOMAINNAME"
vault write pki_int/roles/$VAULT_ENTRA_ID_ROLE_NAME-2048 \
        allowed_domains="$DOMAINNAME" \
        allow_localhost=false \
        allow_subdomains=true \
        key_type=rsa \
        key_bits=2048 \
        max_ttl="17531h"

echo "Create a digital signature role"
vault write pki_int/roles/digital-signature \
        allowed_domains="$DOMAINNAME" \
	    allow_localhost=false \
        allow_subdomains=false \
        allow_bare_domains=true \
        allow_ip_sans=false \
        basic_constraints_valid_for_non_ca=true \
        client_flag=false \
        enforce_hostnames=false \
        key_type=rsa \
        key_bits=4096 \
        key_usage="DigitalSignature" \
        server_flag=false \
        ttl="17531h"

echo "Create a code signing role"
vault write pki_int/roles/code-signing \
	    allow_any_name=true \
        allow_localhost=false \
        allow_subdomains=false \
        allow_bare_domains=false \
        allow_ip_sans=false \
        basic_constraints_valid_for_non_ca=true \
        client_flag=false \
        server_flag=false \
        code_signing_flag=true \
        enforce_hostnames=false \
        key_type=rsa \
        key_bits=4096 \
        key_usage="DigitalSignature" \
        ext_key_usage="CodeSigning" \
        organization="$ORGANIZATION" \
        ttl="17531h"

echo "Create the Docker server and client roles"
vault write pki_int/roles/docker-server \
        max_ttl=8760h \
        ttl=8760h  \
        allowed_domains=$DOMAINNAME \
        allow_localhost=true \
        allow_ip_sans=true \
        allow_bare_domains=false \
        allow_subdomains=true \
        server_flag=true \
        client_flag=false \
        key_type=rsa \
        key_bits=4096 \
        key_usage=DigitalSignature,KeyEncipherment \
        ou="Docker Server"

vault write pki_int/roles/docker-client \
        max_ttl=8760h \
        ttl=720h  \
        allowed_domains=$DOMAINNAME \
        allow_localhost=false \
        allow_ip_sans=false \
        allow_bare_domains=false \
        allow_subdomains=true \
        allow_any_name=false \
        enforce_hostnames=false \
        server_flag=false \
        client_flag=true \
        key_type=rsa \
        key_bits=4096 \
        key_usage=DigitalSignature \
        ou="Docker Client"

echo "Generate a test certificate"
cert_details=$(vault write -format=json pki_int/issue/$VAULT_ENTRA_ID_ROLE_NAME common_name="test.$DOMAINNAME" ttl="1h")

echo $cert_details | jq -r '.data.certificate' > certs/Test.crt
echo $cert_details | jq -r '.data.private_key' > certs/Test.key

# Only run this if you have a machine with openssl installed
# echo "OpenSSL information on the certificate:"
# openssl_cert_details=$(openssl x509 -in certs/Test.crt -text -noout)
# echo $openssl_cert_details

echo "Revoke the test certificate"
vault write pki_int/revoke \
        serial_number=$(echo $cert_details | jq -r '.data.serial_number')

echo "Client - Enabling SSH Signed Certificates"
vault secrets enable -path=ssh-client-signer ssh

echo "Client - Configure Vault with a CA for signing client keys using the /config/ca endpoint"
vault write ssh-client-signer/config/ca generate_signing_key=true

echo "Client - Configure the SSH Signing role"
vault write ssh-client-signer/roles/clientrole @signer-clientrole.json

echo "Client - Sign the public keys"
for filename in client_pub_keys/*.pub; do
    echo "Signing public key '$filename'"
    cat $filename | vault write -format=json ssh-client-signer/sign/clientrole public_key=- | jq -r '.data.signed_key' > "certs/$filename-cert.pub"
done

echo "Server - Enabling SSH Signed Certificates"
vault secrets enable -path=ssh-host-signer ssh

echo "Server - Configure Vault with a CA for signing server keys using the /config/ca endpoint"
vault write ssh-host-signer/config/ca generate_signing_key=true

echo "Server - Extend the host key certificate TTLs"
vault secrets tune -max-lease-ttl=87600h ssh-host-signer

echo "Server - Create role for signing host keys"
vault write ssh-host-signer/roles/hostrole \
    key_type=ca \
    ttl=87600h \
    allow_host_certificates=true \
    algorithm_signer="rsa-sha2-256" \
    allowed_domains="$DOMAINNAME" \
    allow_subdomains=true

echo "Server - Sign the public keys"
for filename in host_pub_keys/*.pub; do
    echo "Signing public key '$filename'"
    cat $filename | vault write -format=json ssh-host-signer/sign/hostrole \
        cert_type=host \
        public_key=- \
        | jq -r '.data.signed_key' > "certs/$filename-cert.pub"
done

echo "Finished..."

echo "Make sure to restart the container since vault logoff command isn't available"
echo "Upon the next container update, the prereqs will be gone as well"
