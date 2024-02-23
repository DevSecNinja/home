# Docker Deployments

## Adding new applications

### Checklist

- [ ] Add the docker compose files to the compose-modules folder
  - [ ] Make sure to add a backup DB container to any applications that need a backup
- [ ] Add any passwords to the secret variables and the .env.j2 file
- [ ] Add the docker compose module to the `compose.yml.j2` file
- [ ] Add the DNS records to the `a-records.conf.j2` file in the unbound folder
