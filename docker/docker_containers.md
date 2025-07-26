# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.63@sha256:320ab49bd5f55091c7da7d1232ed3875f687769d6bb5e55eb891471528e2e18f

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2025.2.1-beta@sha256:d8d510eb726e0c2d265cb1f46f5ee22f208851eef5976efbd27172f1871a570c

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.8.2@sha256:2bcbaec92bd9d4f6591bc8103d3a8e6d0512ee2235506e47a2e129d190444405

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

**image:** amir20/dozzle:v8.13.8@sha256:b6791e8893adce2ea73512b618e0bca2370e77f1ef32848bf6478663633cc31d

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-3.2.3-r0@sha256:63d2e0ce6bb0d12dfdbde5c3af31d08fee343ec3801a050c8197a3f5ffae8bed

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:28.0.7@sha256:fe87cbf35266649d0f1931abc634de0e9cee96415065d20ab04c45fb7445fd67

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

**image:** twinproduction/gatus:v5.19.0@sha256:12362572b78c1bb6f234248de33392a393f7e604d94779e3086ec2dbba1bedf3

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:7c688148e5e156d0e86df7ba8ae5a05a2386aaec1e2ad8e6d11bdf10504b1fb7

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:9682a29fdfde74dd67c78d724105a9c11cb2affaf350192b0a89447f958547df

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.6.1@sha256:c92ee84c9ade9778aa76d35e0e902bea4f148d4b3d8fda5a80056fef14a5da3a

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:7c688148e5e156d0e86df7ba8ae5a05a2386aaec1e2ad8e6d11bdf10504b1fb7

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0@sha256:f36625fffae9611b0e6e28cc1a9bb573d20a9d3cc5e62ab0ff1a19874e34e1f4

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v1.136.0@sha256:198d52734136fe9840866cc2f48a8141e0d002c2a25be7e35cd28ef7936b6c67

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:8-alpine@sha256:0d27f0bca0249f61d060029a6aaf2e16b2c417d68d02a508e1dfb763fa2948b4

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v1.136.0@sha256:8c9633b96ca5b748b10875a99c498ee6f1e5d7f7d1df2bf341909cacb88ad672

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:feb459b8fd785b102c33b56cb3c5bb08c1e91dbfa268379a62a08e26864a0b73

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.101.1@sha256:20f9a5424b44fe24ce86258c70ce1fb3fe8412b01f95314da9733aba9545fd46

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:7c688148e5e156d0e86df7ba8ae5a05a2386aaec1e2ad8e6d11bdf10504b1fb7

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:31.0.7-apache@sha256:31d564f5f9f43f2aed0633854a2abd39155f85aa156997f7252f5af908efa99b

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:31.0.7-apache@sha256:31d564f5f9f43f2aed0633854a2abd39155f85aa156997f7252f5af908efa99b

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.8.2@sha256:2bcbaec92bd9d4f6591bc8103d3a8e6d0512ee2235506e47a2e129d190444405

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:7.4.5-alpine@sha256:bb186d083732f669da90be8b0f975a37812b15e913465bb14d845db72a4e3e08

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/outline.yml

### Service: outline

**container_name:** outline

**image:** outlinewiki/outline:0.85.1@sha256:490b5de174d0f7be9b9d482cf9769b66438d9ce844d12f3c348ba80e36590c0a

**url:** docs.$DOMAINNAME

### Service: outline-db

**container_name:** outline-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:7c688148e5e156d0e86df7ba8ae5a05a2386aaec1e2ad8e6d11bdf10504b1fb7

### Service: outline-db-backup

**container_name:** outline-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: outline-redis

**container_name:** outline-redis

**image:** redis:7.4.5-alpine@sha256:bb186d083732f669da90be8b0f975a37812b15e913465bb14d845db72a4e3e08

### Service: outline-volume-backup

**container_name:** outline-volume-backup

**image:** offen/docker-volume-backup:v2.43.4@sha256:bdb9b5dffee440a7d21b1b210cd704fd1696a2c29d7cbc6f0f3b13b77264a26a

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.2-apache@sha256:c23c54bd48ace4a01761cadd61239ccecd2996a1a893caec6faf96ef08e11d6c

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.9.9961-46083195d@sha256:f8ed359f87f1becab37c2586af9f3414bd5c604d031d47f75e8422baf5224ef5

**url:** plex.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:39952ab247d97c9d3345a572385ebee158ce497887652d8421f4c0ac44cddf7e

**url:** sabnzbd.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.5.2@sha256:1a582590167877ce74bb744fc106136d4ad413a11618fef3ed7ea9a84699e655

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/tubesync.yml

### Service: tubesync

**container_name:** tubesync

**image:** ghcr.io/meeb/tubesync:v0.15.7@sha256:2be1af72b10c97dd78f25d8a64efc43cc6149296c00e0d4b8e93847d9015e264

**url:** tubesync.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.2.87@sha256:0a757b41978541ff9274a311b71437b9c65009f1887d53608011dd3f9a60f02a

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.21@sha256:3d715950d83061ff2fbc910d12d3703212538cacf6b3003e3736fa5c7f51a2e1

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
