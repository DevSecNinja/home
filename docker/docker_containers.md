# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.71@sha256:92929135ced2554aaf94706f766a98ad348f211df61b0704e2db7e8498cc00b7

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

**image:** ghcr.io/gchq/cyberchef:10.19.4@sha256:a2bfe382b2547bdd0a3d0523b9a6b85fab833c56bcec86d600ba6266910b533e

**url:** cyberchef.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/dawarich.yml

### Service: dawarich

**container_name:** dawarich

**image:** freikin/dawarich:0.37.1@sha256:299596d1ddebd47a5baacf271a6d647f7e11d7c13041d5d70430dc61e1be3bd8

**url:** dawarich-noauth.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine@sha256:4294c33e9e52ed2ba617419286923d97ddc5483207cdd5e4d326cc64f0a45c96

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:8.4.0-alpine@sha256:6cbef353e480a8a6e7f10ec545f13d7d3fa85a212cdcc5ffaf5a1c818b9d3798

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:0.37.1@sha256:299596d1ddebd47a5baacf271a6d647f7e11d7c13041d5d70430dc61e1be3bd8

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:29.2.9@sha256:4c064d20674e9ef24b4b7ca1a9b9fb6596d9cd8b2fb7bf042435f23ce4c361c2

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:95d528cb4f8d18e0fbdc42ae3d09b5c4a899bfbd6bb89eeaf94b904330d79714

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

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:6a429e7e047643ca38f25cd0b2e6e3d4b42bf4924a5280a31ab8c907bcf1bbda

## docker/ansible/templates/compose-modules/hadiscover.yml

### Service: hadiscover-api

**container_name:** hadiscover-api

**image:** ghcr.io/devsecninja/hadiscover/backend:0.2.13@sha256:7daa79ec1b01cc17bc619d3848f5c4f78d6879d38a4ba3ab68e96517fe3db860

**url:** api.hadiscover.com

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.12.0@sha256:0bf0d0c1a34399d8bc4a0d89126b41c717db771c5a451d69d076cb4305b9eaff

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:6a429e7e047643ca38f25cd0b2e6e3d4b42bf4924a5280a31ab8c907bcf1bbda

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0@sha256:c570d9e1c2494f65d2a0a379a7f6df66e8441964254a30aa62cc58e8ebf1dee0

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v2.4.1@sha256:b3deefd1826f113824e9d7bc30d905e7f823535887d03f869330946b6db3b44a

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:9-alpine@sha256:c106a0c03bcb23cbdf9febe693114cb7800646b11ca8b303aee7409de005faa8

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v2.4.1@sha256:e6a6298e67ae077808fdb7d8d5565955f60b0708191576143fc02d30ab1389d1

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/lidarr.yml

### Service: lidarr

**container_name:** lidarr

**image:** lscr.io/linuxserver/lidarr:version-3.1.0.4875@sha256:ede2bb17350cc97a0d3f24389aa91803f655eac29aa022c77a71f4a61cc621e4

**url:** lidarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:3c5e59886f404583196a45aa3e3fa9fb7b06e16fcdb71d2db5159b7c4e51b38a

**url:** metube.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:2.2.2@sha256:913ad6aa6dd4c9b3c7990cef306eda98ef8c99fe1a099b1729f5cb1c37ffef44

**url:** n8n.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:6a429e7e047643ca38f25cd0b2e6e3d4b42bf4924a5280a31ab8c907bcf1bbda

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:0.6.43@sha256:9cb724e0bc84f05ba2f81a3da5f53f5add07e1001065d83f3b6b70b9a9eeef19

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.42.2.10156-f737b826c@sha256:1720efa8e919a724ff3003cce7c1c0ae91a54e097ca3c8f6713a780c6fd73432

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/prowlarr.yml

### Service: prowlarr

**container_name:** prowlarr

**image:** lscr.io/linuxserver/prowlarr:version-2.3.0.5236@sha256:67a8aaedcfd6989f3030b937a6a07007310b1dfc7ee8df16d2cbfa48d1c1158c

**url:** prowlarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/qbittorrent.yml

### Service: qbittorrent

**container_name:** qbittorrent

**image:** lscr.io/linuxserver/qbittorrent:5.1.4@sha256:1497b6e047ad47b738f94739219f0e5c5b2ad7a5953b7cf0050f2fedddd8c601

**url:** qbittorrent.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/radarr.yml

### Service: radarr

**container_name:** radarr

**image:** lscr.io/linuxserver/radarr:version-6.0.4.10291@sha256:6c0948b42c149e36bb3dbc0b64d36c77b2d3c9dccf1b424c4f72af1e57ba0c21

**url:** radarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sonarr.yml

### Service: sonarr

**container_name:** sonarr

**image:** lscr.io/linuxserver/sonarr:version-4.0.16.2944@sha256:8b9f2138ec50fc9e521960868f79d2ad0d529bc610aef19031ea8ff80b54c5e0

**url:** sonarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/spottarr.yml

### Service: spottarr

**container_name:** spottarr

**image:** ghcr.io/spottarr/spottarr:1.13.0@sha256:ce70a1c98cb58ea1a30949c9230a7f5ed5fd5dd278eeedb97c224b697eb5e0a2

**url:** spottarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.5.0@sha256:4bc20751924975b6c06589efdb4bbf8db98768abcea361f0d6484873f707ccbc

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.16.1@sha256:f39af04e3a6739f42ae5237ae6420f41a6eb44e7e640cdeb3098d737e1f23bc9

**url:** tubesync.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-10.0.162@sha256:268340299e6a8a85c29800923e242c60ed7baa24557943f0ff5ec4ea52804232

**url:** unifi-guest.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.2.3@sha256:7f5bbdafebde7c42e42e33396d01c0eda3eb753da8dae99071a30e350568a0a4

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
