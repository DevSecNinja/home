# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.72@sha256:4956b35b590286e5872fb4336d84a7862a2030c6efb4ca16442580c37d7ba32d

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/bazarr.yml

### Service: bazarr

**container_name:** bazarr

**image:** lscr.io/linuxserver/bazarr:version-v1.5.3@sha256:001875e61839c8a50743f0bc0fa4da2a55ed8a038b9b5ed0dd2c663dd3d0bfc7

**url:** bazarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.22.1@sha256:3aa4eb2c52c9f9e22bda450cae3187e1de114581f7850d8136c98164837a406c

**url:** cyberchef.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/dawarich.yml

### Service: dawarich

**container_name:** dawarich

**image:** freikin/dawarich:1.1.0@sha256:31aad0680a0da32d60970f0781bdde793b8ba9fc75a744171427767ea0ad358b

**url:** dawarich-noauth.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine@sha256:f494c66c1cb419cd03de1456ae8847879db2f849df3e1567719a02d1bc7ae31c

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:8.6.0-alpine@sha256:fd83658b0e40e2164617d262f13c02ca9ee9e1e6b276fd2fa06617e09bd5c780

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:1.1.0@sha256:31aad0680a0da32d60970f0781bdde793b8ba9fc75a744171427767ea0ad358b

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:29.3.6@sha256:c7c7f7912c2eb5e747978ad4d62a7f21c129df457d2e9711d0abc235993fdfa2

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:3c2513e830bb6e195147c05b34ecf8393d0ba2b1cc86e93b407a5777d6135c6c

**url:** excalidraw.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.34.0@sha256:3fff895e77d35ee62e898860f4613755bc2344127d93e3f326429d40270e2115

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:17.8-alpine@sha256:3430fe182f5065a6ea505c3d432d2c7fff18fbab954df8f277c1dbf4c70124af

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:091e51fb5347d48aec720b139f3b1ede45d4721310274c688cead29e77845921

## docker/ansible/templates/compose-modules/hadiscover.yml

### Service: hadiscover-api

**container_name:** hadiscover-api

**image:** ghcr.io/devsecninja/hadiscover/backend:0.2.14@sha256:cbf696794b817b6fa08345c9fda852da829323f97884b3b48dea3b316d864af4

**url:** api.hadiscover.com

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2026.1.1@sha256:211a005dd4df2bbec15ab684e8c428f073df2da7c6813360225bb37620bdc380

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.8-alpine@sha256:3430fe182f5065a6ea505c3d432d2c7fff18fbab954df8f277c1dbf4c70124af

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:091e51fb5347d48aec720b139f3b1ede45d4721310274c688cead29e77845921

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0@sha256:c570d9e1c2494f65d2a0a379a7f6df66e8441964254a30aa62cc58e8ebf1dee0

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v2.5.6@sha256:b213fa3c82d27a21a299c46ffbb38a091f18384db1ad67d409a3b34fe0fce556

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:9-alpine@sha256:68677f85c863830af7836ff07c4a13b7f085ebeff62f4dedb71499ca27d229f2

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v2.5.6@sha256:aa163d2e1cc2b16a9515dd1fef901e6f5231befad7024f093d7be1f2da14341a

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/lidarr.yml

### Service: lidarr

**container_name:** lidarr

**image:** lscr.io/linuxserver/lidarr:version-3.1.0.4875@sha256:37a3df74f4c2a6f10eead66f4d8034362ebf2866f935026b4a71dd888b9e7f08

**url:** lidarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:4bad68f5d369b3e1deda1edd47f42801e76aa545e72df3405998c0f4c2227f13

**url:** metube.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:2.8.3@sha256:53004142b0e93de1e9e31943e601ed9bd4b24ca82a307864ccadf1820b627e5e

**url:** n8n.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.8-alpine@sha256:3430fe182f5065a6ea505c3d432d2c7fff18fbab954df8f277c1dbf4c70124af

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:091e51fb5347d48aec720b139f3b1ede45d4721310274c688cead29e77845921

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:v0.8.3@sha256:205e9cf23b66553643b065afcdeffb7f86b35bf36e0ce643dc56946a911954b7

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.43.0.10492-121068a07@sha256:bbe0118e39e2c071fc5fe39af3f32072207bf4146d56b6a8901bcb23082df207

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/prowlarr.yml

### Service: prowlarr

**container_name:** prowlarr

**image:** lscr.io/linuxserver/prowlarr:version-2.3.0.5236@sha256:e74a1e093dcc223d671d4b7061e2b4946f1989a4d3059654ff4e623b731c9134

**url:** prowlarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/qbittorrent.yml

### Service: qbittorrent

**container_name:** qbittorrent

**image:** lscr.io/linuxserver/qbittorrent:5.1.4@sha256:85eb27d2d09cd4cb748036a4c7f261321da516b6f88229176cf05a92ccd26815

**url:** qbittorrent.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/radarr.yml

### Service: radarr

**container_name:** radarr

**image:** lscr.io/linuxserver/radarr:version-6.0.4.10291@sha256:6d3e68474ea146f995af98d3fb2cb1a14e2e4457ddaf035aa5426889e2f9249c

**url:** radarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sonarr.yml

### Service: sonarr

**container_name:** sonarr

**image:** lscr.io/linuxserver/sonarr:version-4.0.16.2944@sha256:37be832b78548e3f55f69c45b50e3b14d18df1b6def2a4994258217e67efb1a1

**url:** sonarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/spottarr.yml

### Service: spottarr

**container_name:** spottarr

**image:** ghcr.io/spottarr/spottarr:1.16.0@sha256:bf4663c5d54d47b2beb888bf980f9d6d26457e6939759c193229a2ebff2cbecc

**url:** spottarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.6.1@sha256:dfbce2959ea91ad6855918bf6b41417b6f5b512b23d4bd67f78cc0a62d23f375

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.16.2@sha256:e31f1743b9db2c3deea959a056015b58404f0ddb12f59e6a6fa028aaac704af3

**url:** tubesync.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-10.0.162@sha256:1c3667f6f145b49dcbd105b090a3740a6403f2ae02a164ae9231649e073e2f84

**url:** unifi-guest.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.2.5@sha256:474f5c3bf0e355bb97dafda730e725169a4d51c5578abf7be9ec7ad3fdee4481

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: unifi-volume-backup

**container_name:** unifi-volume-backup

**image:** offen/docker-volume-backup:v2.47.1@sha256:65a395b7531675ebd4ce9fac611da0d954ea628786d683e3d473ce7e65a61769

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
