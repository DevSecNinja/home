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

**image:** freikin/dawarich:0.36.2@sha256:c302b2bec65d8523a4b450b859d89ff348170551317254f9fdbbe22005f38d27

**url:** dawarich-noauth.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine@sha256:d2479a02791972a0210f271de539b69eeeedb5d225e7ff974c5661740d3ed598

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:8.4.0-alpine@sha256:6cbef353e480a8a6e7f10ec545f13d7d3fa85a212cdcc5ffaf5a1c818b9d3798

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:0.36.2@sha256:c302b2bec65d8523a4b450b859d89ff348170551317254f9fdbbe22005f38d27

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

**image:** excalidraw/excalidraw:latest@sha256:b2b642fdaca652cf23c20e07d3603bed5b22b2e1c88a15bec5f92e8a38d9041c

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

**image:** docker.io/library/postgres:17.7-alpine@sha256:7cd12b4b4bf00307d4ab00e98622290e589e5de767cb55a48b1cf0e71770ae24

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:b77b67da5583df5f21d81520477a190c46910c741a3c28d73832adb62d312875

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.11.2@sha256:370f2fa5559b1e82113fb22943a0defd50d49c915439ea3de84fcec9b4b9d690

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:7cd12b4b4bf00307d4ab00e98622290e589e5de767cb55a48b1cf0e71770ae24

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:b77b67da5583df5f21d81520477a190c46910c741a3c28d73832adb62d312875

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

**image:** docker.io/valkey/valkey:9-alpine@sha256:1be494495248d53e3558b198a1c704e6b559d5e99fe4c926e14a8ad24d76c6fa

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

**image:** ghcr.io/alexta69/metube:latest@sha256:153c71f0d7ec031d8e1a3c5dfc501745c2557867a6c40d8c2ce9ab829e5a8708

**url:** metube.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:2.0.2@sha256:e3a4256dd2aa3b987e10da3c1194081575933987b26a604a4f52d2bdd62a5b72

**url:** n8n.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:7cd12b4b4bf00307d4ab00e98622290e589e5de767cb55a48b1cf0e71770ae24

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:b77b67da5583df5f21d81520477a190c46910c741a3c28d73832adb62d312875

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

**image:** lscr.io/linuxserver/plex:version-1.42.2.10156-f737b826c@sha256:ab81c7313fb5dc4d1f9562e5bbd5e5877a8a3c5ca6b9f9fff3437b5096a2b123

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.3.1@sha256:00822205b2901d5ed04420bb0a6eafa815a628f6449317fe60058b08d339b58c

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.15.12@sha256:0885fd4e800fdd9bb0e4103522da3b51ac603dd9852899ed0e749e74c77f92fd

**url:** tubesync.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-10.0.162@sha256:421ef61ced63ccf60a55d0dd4a33f940b97f950a377e1175d60e40b3184cd54f

**url:** unifi-guest.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.2.2@sha256:bf5995bcccb65725aa81fd92e68449323c94b96bf1c1fa9f7acbc2a8ad518114

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
