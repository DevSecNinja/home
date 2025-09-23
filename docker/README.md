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

### Checklist - MongoDB Major Upgrade

This guide covers upgrading MongoDB from one major version to another (e.g., 7.0.21 to 8.0.12). We use `unifi-db` as an example, but these steps apply to any MongoDB instance.

#### Pre-upgrade preparation

- [ ] **Verify application compatibility**: Check the application documentation to confirm it supports the new MongoDB major version
- [ ] **Prepare Renovate commit**: Do not merge the MongoDB Renovate commit yet, but keep the new version and SHA hash readily available
- [ ] **Create VM snapshot**: Despite daily backups, take a VM snapshot for quick rollback if needed
- [ ] **Schedule maintenance window**: Plan for potential downtime during the upgrade process

#### Upgrade procedure

For each MongoDB database in the upgrade:

##### Step 1: Check Feature Compatibility Version (FCV)

- [ ] Login to the applicable Docker server
- [ ] Connect to MongoDB: `docker exec -it unifi-db mongosh`
- [ ] List databases: `show dbs`
- [ ] Check current FCV: `db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })`
    - *Note: FCV supports N-1 and N+1 versions. For example, FCV 6.0 works with MongoDB versions 5.x and 7.x, but not 4.x or 8.x*

##### Step 2: Update Feature Compatibility Version (if needed)

- [ ] Set FCV to target version: `db.adminCommand({ setFeatureCompatibilityVersion: "<X>.0" })` (replace `<X>` with desired major version)
- [ ] If prompted with confirmation warning, re-run with confirmation:

    ```javascript
    db.adminCommand({ setFeatureCompatibilityVersion: "7.0", confirm: true})
    ```

- [ ] Verify command returns `{ ok: 1 }`

##### Step 3: Upgrade MongoDB binaries

- [ ] Stop the application container: `docker stop unifi`
- [ ] Update the MongoDB version in the Docker Compose file
- [ ] Start the database with new version: `docker compose up -d unifi-db --wait`
- [ ] Monitor database logs: `docker logs unifi-db`
    - *Look for: `"msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}`*
- [ ] Check for any upgrade-related errors in the logs

##### Step 4: Validate and restart services

- [ ] Restart the application: `docker compose up -d unifi --wait`
- [ ] Verify application functionality through its interface
- [ ] Test key application features to ensure compatibility
- [ ] Remove VM snapshot once everything is confirmed working

#### Post-upgrade optimization (recommended)

- [ ] **Update FCV to current version** (prevents issues with future upgrades):
    - [ ] Stop application container: `docker stop unifi`
    - [ ] Connect to MongoDB and update FCV to match the running version
    - [ ] Restart database container: `docker compose restart unifi-db`
    - [ ] Verify database connectivity: `docker logs unifi-db`
    - [ ] Restart application: `docker compose up -d unifi --wait`

### Checklist - PostgreSQL Major Upgrade

This guide covers upgrading PostgreSQL from one major version to another (e.g., PostgreSQL 15 to 16). The process varies slightly depending on whether your PostgreSQL instance uses extensions.

#### PostgreSQL pre-upgrade preparation

- [ ] **Verify application compatibility**: Check that your applications support the new PostgreSQL major version
- [ ] **Identify PostgreSQL instances**: Review your compose files to identify all PostgreSQL containers that need upgrading
- [ ] **Check for extensions**: Note any special PostgreSQL images with extensions (e.g., `immich-db` with vector extensions)
- [ ] **Create VM snapshot**: Take a snapshot of the VM hosting the containers for quick rollback
- [ ] **Verify backup status**: Ensure your `tiredofit/db-backup` containers are functioning and recent backups exist
- [ ] **Schedule maintenance window**: Plan for downtime during the upgrade process

#### Backup verification

- [ ] Check recent backup status: `docker logs <service>-db-backup`
- [ ] Verify backup files exist: `ls -la $DOCKERDIR/data/backup/`
- [ ] Note backup encryption status and ensure you have the decryption passphrase

#### PostgreSQL upgrade procedure (Standard PostgreSQL)

For standard PostgreSQL instances (gatus-db, hoppscotch-db, etc.):

##### Step 1: Prepare for upgrade

- [ ] Login to the applicable Docker server
- [ ] Stop the application container: `docker stop <service>`
- [ ] Stop the PostgreSQL container: `docker stop <service>-db`
- [ ] Create a manual backup before proceeding:

    ```bash
    docker run --rm --network <service>-backend \
      -v $DOCKERDIR/data/backup:/backup \
      postgres:16.10-alpine pg_dump -h <service>-db -U <username> <database> > /backup/pre-upgrade-$(date +%Y%m%d).sql
    ```

##### Step 2: Upgrade using dump and restore method

- [ ] Export current data:

    ```bash
    docker run --rm --network <service>-backend \
      -v <service>_db_data:/var/lib/postgresql/data \
      -v $DOCKERDIR/data/backup:/backup \
      postgres:OLD_VERSION pg_dumpall -U <username> > /backup/full-dump-$(date +%Y%m%d).sql
    ```

- [ ] Remove old data volume: `docker volume rm <service>_db_data`
- [ ] Update PostgreSQL version in Docker Compose file
- [ ] Start new PostgreSQL container: `docker compose up -d <service>-db --wait`
- [ ] Restore data:

    ```bash
    docker exec -i <service>-db psql -U postgres < /backup/full-dump-$(date +%Y%m%d).sql
    ```

##### Step 3: Validate upgrade

- [ ] Check PostgreSQL logs: `docker logs <service>-db`
- [ ] Verify database connectivity: `docker exec -it <service>-db psql -U <username> -d <database> -c '\l'`
- [ ] Start application container: `docker compose up -d <service> --wait`
- [ ] Test application functionality through its interface

#### PostgreSQL upgrade procedure (PostgreSQL with extensions)

For PostgreSQL instances with special extensions (like `immich-db`):

##### Step 1: Check extension compatibility

- [ ] Research extension compatibility with new PostgreSQL version
- [ ] Verify the specialized Docker image supports the target PostgreSQL version
- [ ] Note any extension-specific upgrade procedures

##### Step 2: Follow standard upgrade with additional considerations

- [ ] Ensure the new Docker image includes all required extensions
- [ ] After restore, verify extensions are properly loaded:

    ```sql
    SELECT * FROM pg_extension;
    ```

- [ ] Test extension-specific functionality in the application

#### Rollback procedure (if needed)

If the upgrade fails:

- [ ] Stop all containers: `docker stop <service> <service>-db`
- [ ] Restore VM snapshot to previous state
- [ ] Alternatively, restore from backup:
    - [ ] Remove failed data volume: `docker volume rm <service>_db_data`
    - [ ] Revert Docker Compose file to previous PostgreSQL version
    - [ ] Start old PostgreSQL version: `docker compose up -d <service>-db --wait`
    - [ ] Restore from backup: `docker exec -i <service>-db psql -U postgres < /backup/pre-upgrade-<date>.sql`

#### Post-upgrade tasks

- [ ] **Update backup configuration**: Ensure backup containers work with new PostgreSQL version
- [ ] **Update monitoring**: Verify health checks and monitoring still function correctly
- [ ] **Test backup/restore**: Perform a test restore to ensure backup compatibility
- [ ] **Update documentation**: Record any service-specific notes for future upgrades
- [ ] **Remove VM snapshot**: Clean up snapshots once everything is confirmed working
- [ ] **Schedule follow-up check**: Monitor application stability over the next few days
