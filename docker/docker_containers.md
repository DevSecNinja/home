# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.62@sha256:b04764acecf1f663a23f55e95724a3c7ca0dc7f3a6f957d29005728b6bd036f2

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/beaverhabits.yml

### Service: beaverhabits

**container_name:** beaverhabits

**image:** daya0576/beaverhabits:0.4@sha256:390996eb549510e7979bbb9956119b5391184e80be7e9398530b3dd5128ab19b

**url:** habits.$DOMAINNAME

### Service: beaverhabits-db-backup

**container_name:** beaverhabits-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2025.2.1-beta@sha256:d8d510eb726e0c2d265cb1f46f5ee22f208851eef5976efbd27172f1871a570c

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.7.2@sha256:fcc7fcd7114adb5d41f14d116b8aac45f94280d2babfbbb71b4782922ee6d8d4

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.15.1@sha256:a4e2089b3531eec8c9328c7a9a586f80e8d67dcd94856e0b596b7896e1de3f62

## docker/ansible/templates/compose-modules/code-server.yml

### Service: code-server

**container_name:** code-server

**image:** lscr.io/linuxserver/code-server:version-4.89.0@sha256:07c4a16372f79ca1ba65b706082ebfa83a5d13986cd1da4cc936fe6265a2b295

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.19.4@sha256:a2bfe382b2547bdd0a3d0523b9a6b85fab833c56bcec86d600ba6266910b533e

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v8.12.21@sha256:4e4a7ab10dc2db42d401755c780a510072e9b453251529e2457539f9a823400a

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-3.0.10-r0@sha256:426b902e324e63415f23717c98d79c779259d1d7dfd7d6d9b5bd9358d1d93d57

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:27.0.9@sha256:4f9f6cdcce1b820d3a5082e8da0d1342eff7235ef19a9b92244c4276f0ec7d86

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:37@sha256:f55000d9196bd3c853d384af7315f509d21ffb85de315c26e9874033b9f83e15

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:525d72908ffed09807bad50321b94698d725ddc5945118dc3e0b4a494f9772a8

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.18.1@sha256:97525568fdef34539b1b4d015aef2d1cf6f58f1bc087443387b349940544394d

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:2c80c840f66b8fbe7320d3b95ad345ad4864fa6608e3ad296e22aacc88256463

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:e7611af2b9a3251dee92488be1142a889e1600e4587fc10c3228ef9302f4a605

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.5.1@sha256:f7e7671070919d5bfd6e624de3ac01ef0cada5fb9dbf739fa020f8ff7a8d4ac6

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:2c80c840f66b8fbe7320d3b95ad345ad4864fa6608e3ad296e22aacc88256463

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:de75efaa84efe8df92bf1cd85ae6cd7db9ad3b5d6979d1adfe24773a192156c9

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.97.1@sha256:1f42981993b424a9b9bebd620ab220b531612b319b6f7a75a76929e61ab456b1

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:2c80c840f66b8fbe7320d3b95ad345ad4864fa6608e3ad296e22aacc88256463

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:31.0.5-apache@sha256:e775d46d9888d87d11c76bd8c5d19561e99e6975052c4c5bd7f2610392b0cbc7

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:31.0.5-apache@sha256:e775d46d9888d87d11c76bd8c5d19561e99e6975052c4c5bd7f2610392b0cbc7

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.7.2@sha256:fcc7fcd7114adb5d41f14d116b8aac45f94280d2babfbbb71b4782922ee6d8d4

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:8f157725f8eee31e65a8d4765f1f986d76aedc1a0503345dfb63a2b1b5a441ee

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.2-apache@sha256:73467128842bc4406372310f068bc9ccb6727a82c7b5dc9c4f3d815ead33eab8

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.7.9823-59f304c16@sha256:87cf58fff5adfebc97871837198b73bcf255b3551432be39697fbdbbdc58c8f8

**url:** plex.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:0387d9abeda5c7481905dcfd56b62f64ed96ee7d09bbaf5fc9001f328d525b4e

**url:** sabnzbd.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.5.2@sha256:1a582590167877ce74bb744fc106136d4ad413a11618fef3ed7ea9a84699e655

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.15.4@sha256:eccdd1ae2ea38a8f77efcb6528a9b865d1fbf0d9a2e8c918e8cb05e4a7495435

**url:** tubesync.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.1.120@sha256:685dc8ee686f2d35305f0de06b1b1c994a1d68d9e509556875e7feca864bb8f6

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.21@sha256:befd915014332949d8e1f1ddbf8edb1d5066b3f33cded9e0f1e82d5298b52402

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

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
