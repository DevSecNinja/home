# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.71@sha256:92929135ced2554aaf94706f766a98ad348f211df61b0704e2db7e8498cc00b7

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.15.1@sha256:a4e2089b3531eec8c9328c7a9a586f80e8d67dcd94856e0b596b7896e1de3f62

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.19.4@sha256:a2bfe382b2547bdd0a3d0523b9a6b85fab833c56bcec86d600ba6266910b533e

**url:** cyberchef.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/dawarich.yml

### Service: dawarich

**container_name:** dawarich

**image:** freikin/dawarich:latest

**url:** dawarich.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:7.4.5-alpine@sha256:bb186d083732f669da90be8b0f975a37812b15e913465bb14d845db72a4e3e08

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:latest

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:29.2.7@sha256:b2082ee9e1e3f213ab9cac7b428816c5ca2c6eaee471abbc9abe0a041ffe2998

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:38@sha256:c73e039e883944a38e37eaba829eb9a67641cd03eff868827683951feceef96e

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:67c6b93d6155fac09d30759ea5f28e5ce01b4e865a783fb418c878806bf5397d

**url:** excalidraw.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.33.1@sha256:7121b5916c069eac6e266875d4984ec9262d84bd1274963939b358b32476d25b

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:9a78577340f3d26384b6aebeb475c0d46d664fd4ffa68503b4be4e4462745f94

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:9d5f6551a8b5771e0162c36b5ac16b2d6533b439806dfcc1c24928bd383fefd6

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.11.2@sha256:370f2fa5559b1e82113fb22943a0defd50d49c915439ea3de84fcec9b4b9d690

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:9a78577340f3d26384b6aebeb475c0d46d664fd4ffa68503b4be4e4462745f94

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:9d5f6551a8b5771e0162c36b5ac16b2d6533b439806dfcc1c24928bd383fefd6

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0@sha256:c570d9e1c2494f65d2a0a379a7f6df66e8441964254a30aa62cc58e8ebf1dee0

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v2.3.1@sha256:379e31b8c75107b0af8141904baa8cc933d7454b88fdb204265ef11749d7d908

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:9-alpine@sha256:b4ee67d73e00393e712accc72cfd7003b87d0fcd63f0eba798b23251bfc9c394

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v2.3.1@sha256:f8d06a32b1b2a81053d78e40bf8e35236b9faefb5c3903ce9ca8712c9ed78445

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:75c227ff12ffbcb3bcbfe9cb0b8ff067cde30de2771d7992f41d9680ba46fdd9

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.120.3@sha256:e047444709aa5ce8e2be7c952b51d95c35989ea8a36ed7b4ed478c2193df5825

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:9a78577340f3d26384b6aebeb475c0d46d664fd4ffa68503b4be4e4462745f94

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:9d5f6551a8b5771e0162c36b5ac16b2d6533b439806dfcc1c24928bd383fefd6

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:0.6.41@sha256:3e07bcede92e97cc3e741de095045a8b5d20bc257ecdb713bd2a47f68e9dff72

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.42.2.10156-f737b826c@sha256:a4749f3b84dc3f923a7bd4d2bc4ddc1e871b5a656b62022d3827d3d98afd5efd

**url:** plex.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.1.0@sha256:1d01039c168dd88308b670ff2823798f0acbdd1661870cbcb0f46ea46518344c

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.15.12@sha256:0885fd4e800fdd9bb0e4103522da3b51ac603dd9852899ed0e749e74c77f92fd

**url:** tubesync.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.5.21@sha256:f45155f97d755373f5ad06abafa59fd2a5c2df690ae5d9e6d22e69548788c11b

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.2.1@sha256:e64a984d36b24419327c558b49a9100cf78191706222da6a7c8cf56a743ad3db

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: unifi-volume-backup

**container_name:** unifi-volume-backup

**image:** offen/docker-volume-backup:v2.46.1@sha256:039188f012d26178e68a0bb906cd408b9fc197069e8076d03014a31a5fed1406

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
