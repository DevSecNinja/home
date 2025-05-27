# Docker Services

For more information about the Docker services and containers I deploy, see the [docker_containers file.](docker_containers.md)

## Adding new applications

### Checklist - new application

- [ ] Add the docker compose files to the compose-modules folder
    - [ ] Make sure to add a backup DB container to any applications that need a backup
- [ ] Add any passwords to the secret variables and the .env.j2 file
- [ ] Add the docker compose module to the `compose.yml.j2` file
- [ ] Add the DNS records to the `a-records.conf.j2` file in the unbound folder
- [ ] Add an HTTP status check to Gatus `config.yaml` file in the gatus folder

## Installing a new host

### Checklist - new host

- [ ] Create the host via template in Proxmox
- [ ] Make sure the hostname is set correctly
- [ ] Add the host to the `hosts.yaml` file
- [ ] Run the `new-docker-server` playbook
- [ ] Update DNS records in `a-records.conf.j2` for the new host and new apps
- [ ] Now you can run the regular playbook `update-docker`

### Checklist - new Windows Server host

- [ ] Create the host via ISO in Proxmox. Make sure to follow the [official guide](https://pve.proxmox.com/wiki/Windows_2022_guest_best_practices) to also install the needed drivers
- [ ] Set fixed IP in Excel sheet and Unifi portal
    - [ ] NOTE: for some reason, VLAN tagging doesn't seem to work for Windows Server 2022 with a `VirtIO (paravirtualized)` adapter.
- [ ] If needed, set the VLAN tag on the VM
- [ ] Remove the ISO on the VM in Proxmox
- [ ] Change the hostname
- [ ] Enable Remote Desktop

### Checklist - removing a Docker service

- [ ] Make the required changes, Ansible will fail with `service \"traefik\" refers to undefined network <service>-frontend: invalid compose project`
- [ ] Manually remove this network from the host by running:
    - `docker stop <service>`
    - `docker rm <service>`
    - `docker stop traefik` (required as the network is 'taken' by Traefik)
    - `docker network rm <service>-frontend`
- [ ] Re-run Ansible with `task docker:run playbook=update-docker`
