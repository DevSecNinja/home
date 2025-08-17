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


## Upgrading databases

### MongoDB major release

This instruction was created for updating MongoDB 7.0.21 to 8.0.12. We use `unifi-db` as an example:

- [ ] Confirm the application you are running works with the new major version of the database by checking their documentation.
- [ ] Do not merge the mongodb Renovate commit to upgrade to a major version yet, but do keep the version + SHA hash on the clipboard.
- [ ] Despite the daily backups, make sure to take a snapshot of the VM that runs the container for easy restore.

For each of the databases that is included in the Renovate commit:

- [ ] Login on the applicable Docker server
- [ ] Run `docker exec -it unifi-db mongosh` to connect to the MongoDB server
- [ ] Run `show dbs` to view the databases
- [ ] Run `db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })` to check the Feature Compatibility Version. Note that this should be max N-1 and N+1. So if this command returns `{ featureCompatibilityVersion: { version: '6.0' }, ok: 1 }`, the database will work with both version 5 and 7, but not with 8 or 4.
- [ ] Run `test> db.adminCommand({ setFeatureCompatibilityVersion: "<X>.0" })` with the desired version at position X.
- [ ] You might receive a notification like `MongoServerError[Location7369100]: Once you have upgraded to 7.0, you will not be able to downgrade FCV and binary version without support assistance. Please re-run this command with 'confirm: true' to acknowledge this and continue with the FCV upgrade.`. Make sure to run the previous command with `confirm: true`. In this example: `db.adminCommand({ setFeatureCompatibilityVersion: "7.0", confirm: true})`. It should return `{ ok: 1 }`.
- [ ] Stop the application docker container (in this case, `unifi`)
- [ ] Manually add the new MongoDB version to the Docker compose file
- [ ] Run `docker compose up -d unifi-db --wait`
- [ ] Check the logs of the database: `docker logs unifi-db` and look for the log `"msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}`
- [ ] Also check the logs for any post-upgrade errors
- [ ] Run `docker compose up -d unifi --wait` to start the application server. Confirm that the application runs correctly.
- [ ] Remove the VM snapshot if everything runs well.

- [ ] To prevent the next major upgrade to break, consider upgrading the `featureCompatibilityVersion` to the version that the database server is running now.
    - [ ] Stop the application container once more
    - [ ] Rerun the `setFeatureCompatibilityVersion` command
    - [ ] As a precaution, restart the DB container
    - [ ] Check the logs of the database: `docker logs unifi-db` and look for the log `"msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}`
