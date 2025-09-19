# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.66@sha256:cc8757742e547c722bb0bd9a3b11fce22771a75a5b0e07ce9a789ad62a2bfd37

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

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v8.13.14@sha256:f16c49728f7c4ce94a56b1f92b1e0529d6d5c954397a64840426edaf0d5dea4e

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-3.2.4-r0@sha256:eaa680cf252ccf1dea354801f2444728fbfabb6431897aaa57d67bbf2121cce0

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:28.0.9@sha256:8d7f123e0ad2b3ca6ea1282cfe02a2c0c4c2b8e71c542ec6b879b748cfa4de4c

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:37@sha256:f55000d9196bd3c853d384af7315f509d21ffb85de315c26e9874033b9f83e15

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:333be98e977744ca7f457074720fed1ad8b470bdeb699d3fcc4a8622bac83f48

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.23.2@sha256:041514059279f102d8e549a7c7c9f813ae9a0bf505c6d7c37aea9201af0bec3a

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:1c6d2f6e4d30d49c529e09a627e8178db5011dde88d955eb08db2e135e64aa09

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.8.1@sha256:bbf30918d0f58743947fd691a9dd9544d5a37aae313c3909478470b8c72e0396

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:1c6d2f6e4d30d49c529e09a627e8178db5011dde88d955eb08db2e135e64aa09

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:16-vectorchord0.3.0-pgvectors0.2.0@sha256:24e0dd61e4923ec3daa9272aa0660625bafd2012b4a2a32c3cb796f392ec356f

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v1.142.1@sha256:9855f6a0a998db508ca97894997b17f3a0a61e9388b204d861110c19c42814eb

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:8-alpine@sha256:d827e7f7552cdee40cc7482dbae9da020f42bc47669af6f71182a4ef76a22773

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v1.142.1@sha256:06bc7715fa4c4a1641bd0b566c949cd7327f420632b480389fd4d1e70665d046

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:df4b25db48351e58fe732b26a92e5d5b06734e1470894707c659fb1bafd3688e

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.108.1@sha256:8509288ac9c0591ddb8a4e4a8e432e003f3cc91bf492cfed6e2c8125c3de3a94

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:1c6d2f6e4d30d49c529e09a627e8178db5011dde88d955eb08db2e135e64aa09

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:v0.6.30@sha256:b9f7930a5eea6a3284f45ab6d20f9e1e02a5cd6da6b57b962b05422de5233f23

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/outline.yml

### Service: outline

**container_name:** outline

**image:** outlinewiki/outline:0.86.1@sha256:57481d58bcca16493f10644b72a17c508baa7e039abf83208e182cc793525d75

**url:** docs.$DOMAINNAME

### Service: outline-db

**container_name:** outline-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:1c6d2f6e4d30d49c529e09a627e8178db5011dde88d955eb08db2e135e64aa09

### Service: outline-db-backup

**container_name:** outline-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: outline-redis

**container_name:** outline-redis

**image:** redis:8.2.1-alpine@sha256:987c376c727652f99625c7d205a1cba3cb2c53b92b0b62aade2bd48ee1593232

### Service: outline-volume-backup

**container_name:** outline-volume-backup

**image:** offen/docker-volume-backup:v2.44.0@sha256:fcf92e0f192214ccda0a89f989bed6c49d4ed77da4e59b38ddfcf05a05512337

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.2-apache@sha256:23d39937547eebf3cb0d81b9b655e924afb82b5cdd573c9dcd9064b5c0610d4b

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.42.1.10060-4e8b05daf@sha256:3380d8901bf62a9b2246e665d6b8d1f9e03847327b539fb95feef681a8a171ff

**url:** plex.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.6.0@sha256:e76ca5f507d29ca7d5aea38c49f384ea3da4b5b48873dfb77e8b3b2217bd824b

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.15.9@sha256:d919db81e9c552ff56f8efdce61b5b37934c4946354c0f54a589f22e5708572d

**url:** tubesync.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.4.19@sha256:1e59277d29efda7fd024ad1dc72567e46db6530e82e43733044423e9750e4e05

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.0.13@sha256:cf340b1e5283843c63eb12999922f20c463ae31285f746d30f05dcc21cd1d47c

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/whoogle.yml

### Service: whoogle

**container_name:** whoogle

**image:** benbusby/whoogle-search:latest@sha256:b71765b59c96fc1fdd9b770a15c9662b5621f710369d30e42e36bf7af537e4f5

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
