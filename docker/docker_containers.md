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

**image:** freikin/dawarich:0.37.3@sha256:efab2e677baf912f5cc68363ec26e648015fa2c703b4a0cf8e03418415e1ed0d

**url:** dawarich-noauth.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine@sha256:0ccc4f581a6d6016d9ebee67f0496702005e6b5650b710b9ae6edbd5ccf7ceff

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:8.4.0-alpine@sha256:6cbef353e480a8a6e7f10ec545f13d7d3fa85a212cdcc5ffaf5a1c818b9d3798

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:0.37.3@sha256:efab2e677baf912f5cc68363ec26e648015fa2c703b4a0cf8e03418415e1ed0d

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:29.3.5@sha256:f7794421a5a8eb55ff81446b3149bb96d06cd024c662eabdfe18a3fdd74d205b

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

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:c0c6d6021b270bef14cb137f3fbb22582dcc365824551a1a584458738cf2ae4d

## docker/ansible/templates/compose-modules/hadiscover.yml

### Service: hadiscover-api

**container_name:** hadiscover-api

**image:** ghcr.io/devsecninja/hadiscover/backend:0.2.14@sha256:cbf696794b817b6fa08345c9fda852da829323f97884b3b48dea3b316d864af4

**url:** api.hadiscover.com

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.12.1@sha256:8cb58bf214d08360453aa4b4be748295e4c8a8abedc22850bc800272d9c41850

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:c0c6d6021b270bef14cb137f3fbb22582dcc365824551a1a584458738cf2ae4d

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

**image:** lscr.io/linuxserver/lidarr:version-3.1.0.4875@sha256:be65454ba890ad01a93b01cfc178adfa1a397b487bfdce2ac23bd956c473d10d

**url:** lidarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:dbbf9a25660b6255cc0726a00c06cf2968941803e29813e1d23863919794713c

**url:** metube.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:2.5.2@sha256:54c34f83b2294f3bef7fd684913873f575e51975e7443cf835dce5ede8a175df

**url:** n8n.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:c0c6d6021b270bef14cb137f3fbb22582dcc365824551a1a584458738cf2ae4d

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:0.7.2@sha256:16d9a3615b45f14a0c89f7ad7a3bf151f923ed32c2e68f9204eb17d1ce40774b

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.42.2.10156-f737b826c@sha256:b19a5e34c6f8dd42abf88556b8aa5c8987c0c34820aaeaa320a02d8c17fdaab3

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/prowlarr.yml

### Service: prowlarr

**container_name:** prowlarr

**image:** lscr.io/linuxserver/prowlarr:version-2.3.0.5236@sha256:d3e9307b320b6772749a2cf8fc2712e9e824c4930b034680ad4d08a9e2f25884

**url:** prowlarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/qbittorrent.yml

### Service: qbittorrent

**container_name:** qbittorrent

**image:** lscr.io/linuxserver/qbittorrent:5.1.4@sha256:f430d70c70d1547fded30fbc3181c4750cef354212a5138ab754eba9ba8bd9e1

**url:** qbittorrent.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/radarr.yml

### Service: radarr

**container_name:** radarr

**image:** lscr.io/linuxserver/radarr:version-6.0.4.10291@sha256:270f25698624b57b86ca119cc95399d7ff15be8297095b4e1223fd5b549b732c

**url:** radarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/sonarr.yml

### Service: sonarr

**container_name:** sonarr

**image:** lscr.io/linuxserver/sonarr:version-4.0.16.2944@sha256:02b4d538d351d6e35882a021c08e8600fe95d28860fb1dd724b597166e7221ca

**url:** sonarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/spottarr.yml

### Service: spottarr

**container_name:** spottarr

**image:** ghcr.io/spottarr/spottarr:1.14.0@sha256:0b790654ab2b1f7eed75afd23d7f76aafeb9360f0e96e163f09d4d480b3380ad

**url:** spottarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.6.0@sha256:bb9475ea74de9befca2730bd56e4c97a1d333fb5cc250382dcf39ba92a974f8a

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.16.1@sha256:f39af04e3a6739f42ae5237ae6420f41a6eb44e7e640cdeb3098d737e1f23bc9

**url:** tubesync.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-10.0.162@sha256:7948b8c2ca4cd9bf9e1839f3e399c320e0a8318cd54dc807c247f48702f4b157

**url:** unifi-guest.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.2.3@sha256:d6b569590880bca35e43318418133a426b024bcb649eeb63bb071bc1490bee41

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: unifi-volume-backup

**container_name:** unifi-volume-backup

**image:** offen/docker-volume-backup:v2.47.0@sha256:2017b0e180cfe7f896117e2c10a05d6036c396de426112875456b808d8a51c6b

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
