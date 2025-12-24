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

**image:** lscr.io/linuxserver/bazarr:version-v1.5.3@sha256:648f694532a3a53d8cf78bc888919ef538659bad41af4c680b0427ad1047d171

**url:** bazarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

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

**image:** freikin/dawarich:0.36.3@sha256:4f83ccbfcbc5166ba9f96ba7571ab0812c2596f99079ceffc7808a3f896bef0b

**url:** dawarich-noauth.$DOMAINNAME

### Service: dawarich-db

**container_name:** dawarich-db

**image:** postgis/postgis:17-3.5-alpine@sha256:8353c2cb385e2ba5b33e09e2158ed820316642b4eebd0502c80ce0bcdb29fcb3

### Service: dawarich-db-backup

**container_name:** dawarich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: dawarich-redis

**container_name:** dawarich-redis

**image:** redis:8.4.0-alpine@sha256:6cbef353e480a8a6e7f10ec545f13d7d3fa85a212cdcc5ffaf5a1c818b9d3798

### Service: dawarich-sidekiq

**container_name:** dawarich-sidekiq

**image:** freikin/dawarich:0.36.3@sha256:4f83ccbfcbc5166ba9f96ba7571ab0812c2596f99079ceffc7808a3f896bef0b

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:29.2.9@sha256:e4e09123e7b296e7a8d19eda122daed1f0e99be8374981a62b5131efa605c2ee

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:38@sha256:c73e039e883944a38e37eaba829eb9a67641cd03eff868827683951feceef96e

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

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

**image:** twinproduction/gatus:v5.33.1@sha256:7121b5916c069eac6e266875d4984ec9262d84bd1274963939b358b32476d25b

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: gatus-db-upgrade

**container_name:** gatus-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:7f11675003847f629f48d2d9dee36fecad7bc39c8037b2371641c5e8b1faacb2

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.11.2@sha256:370f2fa5559b1e82113fb22943a0defd50d49c915439ea3de84fcec9b4b9d690

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: hoppscotch-db-upgrade

**container_name:** hoppscotch-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:7f11675003847f629f48d2d9dee36fecad7bc39c8037b2371641c5e8b1faacb2

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

**image:** docker.io/valkey/valkey:9-alpine@sha256:1be494495248d53e3558b198a1c704e6b559d5e99fe4c926e14a8ad24d76c6fa

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

**image:** ghcr.io/alexta69/metube:latest@sha256:9a2e1292c574dd1c2a2b51ead3e23fd143e071a38d0dc8d2f81ffcb4d265ba11

**url:** metube.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:2.2.1@sha256:ee59276d9d5c7daa97462830cfae12d71cea55adcad705e1756e0c616fcf26b9

**url:** n8n.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:17.7-alpine@sha256:ff4ccc02b97e0ebb6b328ef9ff92522f95586f83be6801896b615088defc8ad2

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: n8n-db-upgrade

**container_name:** n8n-db-upgrade

**image:** pgautoupgrade/pgautoupgrade:17.7-alpine@sha256:7f11675003847f629f48d2d9dee36fecad7bc39c8037b2371641c5e8b1faacb2

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

**image:** lscr.io/linuxserver/plex:version-1.42.2.10156-f737b826c@sha256:7cc7874ad35b105fe1fe4d99ef27be9c5eb2f4115ccf91af5a7283cae0024599

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/prowlarr.yml

### Service: prowlarr

**container_name:** prowlarr

**image:** lscr.io/linuxserver/prowlarr:version-2.3.0.5236@sha256:67a8aaedcfd6989f3030b937a6a07007310b1dfc7ee8df16d2cbfa48d1c1158c

**url:** prowlarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/qbittorrent.yml

### Service: qbittorrent

**container_name:** qbittorrent

**image:** lscr.io/linuxserver/qbittorrent:5.1.4@sha256:043498de39c3dd63eec94360c5ad966a51271d1581070f42cb73ab0cf4776f29

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

**image:** lscr.io/linuxserver/sonarr:version-4.0.16.2944@sha256:60e5edcac39172294ad22d55d1b08c2c0a9fe658cad2f2c4d742ae017d7874de

**url:** sonarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/spottarr.yml

### Service: spottarr

**container_name:** spottarr

**image:** ghcr.io/spottarr/spottarr:1.12.1@sha256:b773a1fbd3c7684d2cc59e61e5790888efb02cdcd09dd1b75aebcf3f59c82dd0

**url:** spottarr.$DOMAINNAME`) && Header(`X-Monitor-Key`, `$GENERIC_MONITORING_HEADER_SECRET

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:4.4.0@sha256:d012b79e6a7494c94577c7da2566fd31d12ae337b908cc724ed0df10d5ab1c36

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
