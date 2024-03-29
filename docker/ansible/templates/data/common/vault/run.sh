#!/bin/bash

# Changing directory to the /config directory where the volume is mounted
cd /config

read -p "Go to $VAULT_ADDR/ui/ for the setup. Press enter to continue"

VAULT_RETRIES=5
echo "Vault is starting..."
until vault status > /dev/null 2>&1 || [ "$VAULT_RETRIES" -eq 0 ]; do
        echo "Waiting for vault to start...: $((VAULT_RETRIES--))"
        sleep 1
done

echo "Authenticating to vault..."
vault login

echo "Enabling Entra ID Authentication"
vault auth enable oidc
vault write auth/oidc/config \
        oidc_discovery_url="$AZURE_AD_DISCOVERY_URL" \
        oidc_client_id="$AZURE_AD_CLIENT_ID" \
        oidc_client_secret="$AZURE_AD_CLIENT_SECRET" \
        default_role="reader"

vault write auth/oidc/role/reader \
        user_claim="sub" \
        oidc_scopes="https://graph.microsoft.com/.default" \
        policies=default \
        ttl=1h \
        allowed_redirect_uris="http://localhost:8250/oidc/callback" \
        allowed_redirect_uris="https://localhost:8250/oidc/callback" \
        allowed_redirect_uris="$VAULT_ADDR/ui/vault/auth/oidc/oidc/callback"
        # groups_claim="groups" # Should be commented because I'm in too many groups

vault write auth/oidc/role/admin \
        user_claim="sub" \
        oidc_scopes="https://graph.microsoft.com/.default" \
        policies=admin \
        ttl=1h \
        allowed_redirect_uris="http://localhost:8250/oidc/callback" \
        allowed_redirect_uris="https://localhost:8250/oidc/callback" \
        allowed_redirect_uris="$VAULT_ADDR/ui/vault/auth/oidc/oidc/callback"
        # groups_claim="groups" # Should be commented because I'm in too many groups

echo "Set admin policy"
vault policy write admin /admin-policy.hcl

echo "Initializing certificate services"
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

vault secrets enable -path=pki_int pki
vault secrets tune -max-lease-ttl=43800h pki_int

echo "Generating the Root CA"
vault write -field=certificate pki/root/generate/internal \
        common_name="$ROOT_CA_COMMON_NAME" \
        key_bits=4096 \
        ttl=87600h > Root_CA.crt

echo "Configuring the Root CA URLs"
vault write pki/config/urls \
        issuing_certificates="$VAULT_ADDR_HTTP/v1/pki/ca" \
        crl_distribution_points="$VAULT_ADDR_HTTP/v1/pki/crl"

echo "Generating the Intermediate CA CSR"
vault write -format=json pki_int/intermediate/generate/internal \
        common_name="$INT_CA_COMMON_NAME" \
        key_bits=4096 \
        | jq -r '.data.csr' > Int_CA.csr

echo "Configuring the Intermediate CA URLs"
vault write pki_int/config/urls \
        issuing_certificates="$VAULT_ADDR_HTTP/v1/pki_int/ca" \
        crl_distribution_points="$VAULT_ADDR_HTTP/v1/pki_int/crl"

echo "Sign the Intermediate CA certificate"
vault write -format=json pki/root/sign-intermediate csr=@Int_CA.csr \
        format=pem_bundle ttl="43800h" \
        | jq -r '.data.certificate' > Int_CA.pem

echo "Import the Intermediate CA back into the vault"
vault write pki_int/intermediate/set-signed certificate=@Int_CA.pem

echo "Create the server certificate role for $DOMAINNAME"
vault write pki_int/roles/$VAULT_AZURE_AD_ROLE_NAME \
        allowed_domains="$DOMAINNAME" \
        allow_localhost=false \
        allow_subdomains=true \
        key_type=rsa \
        key_bits=4096 \
        max_ttl="17531h"

echo "Create the legacy server certificate role for $DOMAINNAME"
vault write pki_int/roles/$VAULT_AZURE_AD_ROLE_NAME-2048 \
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

echo "Generate a test certificate"
cert_details=$(vault write -format=json pki_int/issue/$VAULT_AZURE_AD_ROLE_NAME common_name="test.$DOMAINNAME" ttl="1h")

echo $cert_details | jq -r '.data.certificate' > Test.crt
echo $cert_details | jq -r '.data.private_key' > Test.key

echo "OpenSSL information on the certificate:"
openssl_cert_details=$(openssl x509 -in Test.crt -text -noout)
echo $openssl_cert_details

echo "Revoke the test certificate"
vault write pki_int/revoke \
        serial_number=$(echo $cert_details | jq -r '.data.serial_number')

echo "Client - Enabling SSH Signed Certificates"
vault secrets enable -path=ssh-client-signer ssh

echo "Client - Configure Vault with a CA for signing client keys using the /config/ca endpoint"
vault write ssh-client-signer/config/ca generate_signing_key=true

echo "Client - Configure the SSH Signing role"
vault write ssh-client-signer/roles/clientrole @/signer-clientrole.json

echo "Client - Sign the public keys"
for filename in /data/client_pub_keys/*.pub; do
        echo "Signing public key '$filename'"
        cat $filename | vault write -format=json ssh-client-signer/sign/clientrole public_key=- | jq -r '.data.signed_key' > "$filename-cert.pub"
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
for filename in /data/host_pub_keys/*.pub; do
        echo "Signing public key '$filename'"
        cat $filename | vault write -format=json ssh-host-signer/sign/hostrole \
                cert_type=host \
                public_key=- \
                | jq -r '.data.signed_key' > "$filename-cert.pub"
done

echo "Finished..."
