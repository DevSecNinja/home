#!/bin/bash

# Stop on error
set -e

if [ -z "$SUBSCRIPTION" ]; then
  echo "SUBSCRIPTION is not set. Please set it in the secrets.sops.yml file and make sure to run the script via task talos:create-az-vm."
  exit 1
fi

if [ -z "$STORAGE_ACCOUNT" ]; then
  echo "STORAGE_ACCOUNT is not set. Please set it in the secrets.sops.yml file and make sure to run the script via task talos:create-az-vm."
  exit 1
fi

# Storage container to upload to
export STORAGE_CONTAINER="talos-image"

# Resource group name
export GROUP="rg-k8s"

# Location
export LOCATION="westeurope"

#export WORKER_COUNT=1
export CONTROL_PLANE_COUNT=1

# Get my current external IP (dynamic)
export MY_IP=$(curl -s https://ifconfig.me)

# Internal VNET CIDR
export INTERNAL_CIDR="10.0.0.0/16"

# Change to the right subscription
az account set --subscription $SUBSCRIPTION

# Create resource group, storage account and container
az group create --name $GROUP --location $LOCATION

az storage account create --name $STORAGE_ACCOUNT \
                          --resource-group $GROUP \
                          --location $LOCATION \
                          --sku Standard_LRS

az storage container create --name $STORAGE_CONTAINER \
                            --account-name $STORAGE_ACCOUNT \
                            --public-access off

# Get storage account connection string based on info above
export CONNECTION=$(az storage account show-connection-string \
                    -n $STORAGE_ACCOUNT \
                    -g $GROUP \
                    -o tsv)

# # Download Talos image for Azure AMD64
if [ -f /tmp/talos-azure-amd64.vhd.xz ]; then
    echo "Talos image already downloaded"
else
    echo "Downloading Talos image for Azure AMD64"
    wget https://factory.talos.dev/image/376567988ad370138ad8b2698212367b8edcb69b5fd68c80be1f2ec7d603b4ba/v1.11.2/azure-amd64.vhd.xz -O /tmp/talos-azure-amd64.vhd.xz
fi

# Check if already unpacked
if [ -f /tmp/talos-azure-amd64.vhd ]; then
    echo "Talos image already extracted"
else
    echo "Extracting Talos image for Azure AMD64"
    xz -d /tmp/talos-azure-amd64.vhd.xz

    az storage blob upload \
    --connection-string $CONNECTION \
    --container-name $STORAGE_CONTAINER \
    -f //tmp/talos-azure-amd64.vhd \
    -n talos-azure.vhd

    az image create \
    --name talos \
    --source https://$STORAGE_ACCOUNT.blob.core.windows.net/$STORAGE_CONTAINER/talos-azure.vhd \
    --os-type linux \
    -g $GROUP
fi

# Create vnet
az network vnet create \
  --resource-group $GROUP \
  --location $LOCATION \
  --address-prefix $INTERNAL_CIDR \
  --name talos-vnet \
  --subnet-name talos-subnet

# Create network security group
az network nsg create -g $GROUP -n talos-sg

# Allow apid (Talos API) only from my IP
az network nsg rule create \
  -g $GROUP \
  --nsg-name talos-sg \
  -n apid \
  --priority 1001 \
  --direction inbound \
  --protocol Tcp \
  --source-address-prefixes [$INTERNAL_CIDR,${MY_IP}/32] \
  --destination-port-ranges 50000 \
  --access Allow

# Allow Kubernetes API only from my IP
az network nsg rule create \
  -g $GROUP \
  --nsg-name talos-sg \
  -n kube \
  --priority 1002 \
  --direction inbound \
  --protocol Tcp \
  --source-address-prefixes [$INTERNAL_CIDR,${MY_IP}/32] \
  --destination-port-ranges 6443 \
  --access Allow

# Allow internal cluster communication for trustd and etcd
az network nsg rule create \
  -g $GROUP \
  --nsg-name talos-sg \
  -n trustd-internal \
  --priority 1003 \
  --direction inbound \
  --protocol Tcp \
  --source-address-prefixes $INTERNAL_CIDR \
  --destination-port-ranges 50001 \
  --access Allow

az network nsg rule create \
  -g $GROUP \
  --nsg-name talos-sg \
  -n etcd-internal \
  --priority 1004 \
  --direction inbound \
  --protocol Tcp \
  --source-address-prefixes $INTERNAL_CIDR \
  --destination-port-ranges 2379-2380 \
  --access Allow

# Create public ip
az network public-ip create \
  --resource-group $GROUP \
  --name talos-public-ip \
  --allocation-method static

# Create lb
az network lb create \
  --resource-group $GROUP \
  --name talos-lb \
  --public-ip-address talos-public-ip \
  --frontend-ip-name talos-fe \
  --backend-pool-name talos-be-pool

# Create health check
az network lb probe create \
  --resource-group $GROUP \
  --lb-name talos-lb \
  --name talos-lb-health \
  --protocol tcp \
  --port 6443

# Create lb rule for 6443
az network lb rule create \
  --resource-group $GROUP \
  --lb-name talos-lb \
  --name talos-6443 \
  --protocol tcp \
  --frontend-ip-name talos-fe \
  --frontend-port 6443 \
  --backend-pool-name talos-be-pool \
  --backend-port 6443 \
  --probe-name talos-lb-health

for ((i=0;i<=CONTROL_PLANE_COUNT-1;i++)); do
  # Create public IP for each nic
  az network public-ip create \
    --resource-group $GROUP \
    --name talos-controlplane-public-ip-$i \
    --allocation-method static

  # Create nic
  az network nic create \
    --resource-group $GROUP \
    --name talos-controlplane-nic-$i \
    --vnet-name talos-vnet \
    --subnet talos-subnet \
    --network-security-group talos-sg \
    --public-ip-address talos-controlplane-public-ip-$i\
    --lb-name talos-lb \
    --lb-address-pools talos-be-pool
done

LB_PUBLIC_IP=$(az network public-ip show \
              --resource-group $GROUP \
              --name talos-public-ip \
              --query "ipAddress" \
              --output tsv)

# Check if talos-k8s-azure directory exists
if [ -d "talos-k8s-azure" ]; then
    echo "talos-k8s-azure directory already exists, skipping config creation..."
else
    echo "Creating talos-k8s-azure directory and generating config..."
    mkdir talos-k8s-azure
    talosctl gen config talos-k8s-azure https://${LB_PUBLIC_IP}:6443 --output-dir talos-k8s-azure
fi

# Create availability set
az vm availability-set create \
  --name talos-controlplane-av-set \
  -g $GROUP

# Create the controlplane nodes
# VM Size needs to support V1
# TODO: Test Talos on Az Generation 2 VMs with Secure Boot.
echo "Creating $CONTROL_PLANE_COUNT control plane nodes..."
for ((i=0;i<=CONTROL_PLANE_COUNT-1;i++)); do
  az vm create \
    --name talos-controlplane-$i \
    --image talos \
    --resource-group $GROUP \
    --admin-username talos \
    --generate-ssh-keys \
    --verbose \
    --boot-diagnostics-storage $STORAGE_ACCOUNT \
    --os-disk-size-gb 20 \
    --nics talos-controlplane-nic-$i \
    --availability-set talos-controlplane-av-set \
    --size Standard_D4as_v5 \
    --custom-data ./talos-k8s-azure/controlplane.yaml \
    # --no-wait
done

# # Create worker node
#   az vm create \
#     --name talos-worker-0 \
#     --image talos \
#     --vnet-name talos-vnet \
#     --subnet talos-subnet \
#     -g $GROUP \
#     --admin-username talos \
#     --generate-ssh-keys \
#     --verbose \
#     --boot-diagnostics-storage $STORAGE_ACCOUNT \
#     --nsg talos-sg \
#     --os-disk-size-gb 20 \
#     # --no-wait
#     # --custom-data ./talos-k8s-azure/worker.yaml \ # Instead of the generated config, we'll use the one from this repo

# NOTES:
# `--admin-username` and `--generate-ssh-keys` are required by the az cli,
# but are not actually used by talos
# `--os-disk-size-gb` is the backing disk for Kubernetes and any workload containers
# `--boot-diagnostics-storage` is to enable console output which may be necessary
# for troubleshooting

CONTROL_PLANE_0_IP=$(az network public-ip show \
                    --resource-group $GROUP \
                    --name talos-controlplane-public-ip-0 \
                    --query "ipAddress" \
                    --output tsv)

printf "%s\n" "Control plane 0 IP: $CONTROL_PLANE_0_IP"
printf "%s\n" "Load balancer IP: $LB_PUBLIC_IP"

echo "You can now use this IP in setting up your k8s cluster from the cluster-template in this repository. Or if you have provided custom-data files, proceed to bootstrap the cluster by continuing."

printf "%s " "Press enter to continue"
read ans

talosctl --talosconfig talos-k8s-azure/talosconfig config endpoint $CONTROL_PLANE_0_IP
talosctl --talosconfig talos-k8s-azure/talosconfig config node $CONTROL_PLANE_0_IP

talosctl --talosconfig talos-k8s-azure/talosconfig bootstrap

talosctl --talosconfig talos-k8s-azure/talosconfig kubeconfig .

printf "%s " "Want to remove the local talos image files? Only do this when you are done deploying..."
read ans

# Remove the image download + extract
rm -f /tmp/talos-azure-amd64.vhd.xz
rm -f /tmp/talos-azure-amd64.vhd
