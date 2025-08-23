# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.65@sha256:d765078d2140b464ce837128a4f536f80b4c9ab7fd5b6833ae690b72fae40897

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

**image:** amir20/dozzle:v8.13.9@sha256:e1db2e3040372a9ed52f00049a02b8b76d7750feee4dce77a8915db08708a07c

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-3.2.3-r0@sha256:f678a19b06ffb54ae5c479aa55b915bbc3bc7d217bd785b6ce3fad6134759f24

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

**image:** excalidraw/excalidraw:latest@sha256:712cd4e7383509ffa50998e743d1a0d02b5aa8eeae714e4d073b7cfb7884f15c

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.22.0@sha256:e38fb2489230da144ef85f6892dab9db84e415bdffdf0c6b995ba421d1b6bf3e

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:8ffca822c1933bdc8be7dbbe9c2330974bdb43f5027f47717772fa35925412b0

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.7.1@sha256:82f47708304db43ecbb866e68a79d30aef707bfa3cdc233006f798a7e676145a

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:8ffca822c1933bdc8be7dbbe9c2330974bdb43f5027f47717772fa35925412b0

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:16-vectorchord0.3.0-pgvectors0.2.0@sha256:61c6cc4d89605fc0900cfe9e607717b0409d12f4da284827d452c3e3f19f3335

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v1.138.1@sha256:f34e855424fd91c5990132e5b2bde91e1d178ec5205de293ebd8779839a4a77c

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:8-alpine@sha256:d827e7f7552cdee40cc7482dbae9da020f42bc47669af6f71182a4ef76a22773

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v1.138.1@sha256:1d303559b4c7c6b4ea3cea2276279e4cafdf605c624625674924a6ac04f263cb

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:3eb6cf27932d14a3ead8a6ba28f54c5d2fde22c0cf929a0362985bddbf0ea640

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.107.2@sha256:49e155af65aef02cb5dd6d39eed22f6e078b1cd567836bc02c8a1616ee2a6017

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.10-alpine@sha256:8ffca822c1933bdc8be7dbbe9c2330974bdb43f5027f47717772fa35925412b0

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/open-webui.yml

### Service: open-webui

**container_name:** open-webui

**image:** ghcr.io/open-webui/open-webui:v0.6.25@sha256:1c2c3e7e84d5bb0b5471e4de881539cf39e724835a5c53b252518e82ea0c568e

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

**image:** docker.io/library/postgres:16.10-alpine@sha256:8ffca822c1933bdc8be7dbbe9c2330974bdb43f5027f47717772fa35925412b0

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

**image:** phpmyadmin:5.2.2-apache@sha256:bb1f68d134bc4c99881f1228c53f91de28f06f02fb953ae7603c963be3c8a988

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.42.1.10060-4e8b05daf@sha256:28f18c27b6822328df994154dbf7c0f511032d9f91bbd10881030b706afd8593

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

**image:** ghcr.io/meeb/tubesync:v0.15.8@sha256:0fc34dad5c41c8125668b31dbdb21af4307d5d58913ab918d32c7c7288090c6c

**url:** tubesync.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.3.45@sha256:022dc69b44c28f39d6beb4a269a02f4d0794ec4513d0625eaa2357f4974fdd7f

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:8.0.13@sha256:bf41aa48a1cc0ccc8e6071236acfc428b7110ec2cf14b47c8961bc472e2c7c61

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.21@sha256:36e7888e4887e57e3ab3ec5ecd4782f345226084df6d3fdd93b2d3e4a2162274

## docker/ansible/templates/compose-modules/whoogle.yml

### Service: whoogle

**container_name:** whoogle

**image:** benbusby/whoogle-search:latest@sha256:b5e3f34b60aeead5f96f2ff5a6607c3f5afc4574d2bba964e8d01d6d78d25aa3

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
