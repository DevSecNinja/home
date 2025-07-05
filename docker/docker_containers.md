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

**image:** mariadb:11.8.2@sha256:1e4ec03d1b73af8e7a63137b8ef4820ac7d54c654a1e99eb76235f210f7f0a06

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

**image:** amir20/dozzle:v8.13.4@sha256:36707d180462e764eac81aac793f8352296048404fa4dea1f280fa3cefa7fce3

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-3.2.1-r0@sha256:2f43ca3448409aca133003ff2f7a23b4911e74c4e8a94a24a5a564b89902494e

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:27.1.6@sha256:1e4e1b0419b4e86e42bb1678683aea7a262e3ddae5c9a162eafc14313afb803e

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

**image:** docker.io/library/postgres:16.9-alpine@sha256:ef2235fd13b6cb29728a98ee17862ff5c9b7d20515a9b34804da4a45062695f6

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:e876528e4159974e844bbf3555e67ff48d73a78bf432b717dd9d178328230b40

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.6.0@sha256:0cf0077e618c0a9c04f52deb2ae1e49116a6234984b3e0e39cf338dec2e58f0b

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:ef2235fd13b6cb29728a98ee17862ff5c9b7d20515a9b34804da4a45062695f6

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/immich.yml

### Service: immich-db

**container_name:** immich-db

**image:** ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0@sha256:007a98749340534a0408a26435b1a0ab5ded76df788f897fdb6342c9c1b95448

### Service: immich-db-backup

**container_name:** immich-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: immich-machine-learning

**container_name:** immich-machine-learning

**image:** ghcr.io/immich-app/immich-machine-learning:v1.135.3@sha256:9f2f61d86af82d04926f9b896c995c502303052905517c5485dd26bf1e42a44e

### Service: immich-redis

**container_name:** immich-redis

**image:** docker.io/valkey/valkey:8-alpine@sha256:81681ebc32ea2ce5153094084ca541861168ff588b4b0db998046fc896b99ba7

### Service: immich-server

**container_name:** immich-server

**image:** ghcr.io/immich-app/immich-server:v1.135.3@sha256:df5bbf4e29eff4688063a005708f8b96f13073200b4a7378f7661568459b31e9

**url:** photos.$DOMAINNAME

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/metube.yml

### Service: metube

**container_name:** metube

**image:** ghcr.io/alexta69/metube:latest@sha256:6ca874e368e4f54d0a586a0c24b1bc8ade386b5505a7214ffef4edff11514beb

**url:** metube.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.101.1@sha256:20f9a5424b44fe24ce86258c70ce1fb3fe8412b01f95314da9733aba9545fd46

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:ef2235fd13b6cb29728a98ee17862ff5c9b7d20515a9b34804da4a45062695f6

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:31.0.6-apache@sha256:588609d76b217cfd0feda653eea9894eeb12e612b327d2f1dcd38221ad242be0

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:31.0.6-apache@sha256:588609d76b217cfd0feda653eea9894eeb12e612b327d2f1dcd38221ad242be0

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.8.2@sha256:1e4ec03d1b73af8e7a63137b8ef4820ac7d54c654a1e99eb76235f210f7f0a06

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:7.4.4-alpine@sha256:ee9e8748ace004102a267f7b8265dab2c618317df22507b89d16a8add7154273

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/outline.yml

### Service: outline

**container_name:** outline

**image:** outlinewiki/outline:0.85.0@sha256:ffe0737c606a2b4e36b79eb850bf2a9e86ea642bea03d08f1abb2286b4ebfcb6

**url:** docs.$DOMAINNAME

### Service: outline-db

**container_name:** outline-db

**image:** docker.io/library/postgres:16.9-alpine@sha256:ef2235fd13b6cb29728a98ee17862ff5c9b7d20515a9b34804da4a45062695f6

### Service: outline-db-backup

**container_name:** outline-db-backup

**image:** tiredofit/db-backup:4.1.19@sha256:26eca0cda2b5decb4e296917f9aaebda2e6f89a237663a65e1cb3eccfe432cd0

### Service: outline-redis

**container_name:** outline-redis

**image:** redis:7.4.4-alpine@sha256:ee9e8748ace004102a267f7b8265dab2c618317df22507b89d16a8add7154273

### Service: outline-volume-backup

**container_name:** outline-volume-backup

**image:** offen/docker-volume-backup:v2.43.4@sha256:bdb9b5dffee440a7d21b1b210cd704fd1696a2c29d7cbc6f0f3b13b77264a26a

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.2-apache@sha256:167d118153d351966f8a245b7d0dbaeaa9c1b26d52bddb19f452b4ba21d4364d

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.8.9834-071366d65@sha256:14e8d783f2b0ec7e7ca2836d3d7185f5e68c60ba0e4eac77666bee4f0f819043

**url:** plex.$DOMAINNAME

## docker/ansible/templates/compose-modules/sabnzbd.yml

### Service: sabnzbd

**container_name:** sabnzbd

**image:** docker.io/linuxserver/sabnzbd:amd64-4.5.1@sha256:95a3cec22c92c6cd8f74f26748e04d97ff4e44c212b10956a8413e26510492c0

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

**image:** lscr.io/linuxserver/unifi-network-application:version-9.2.87@sha256:9d10634136c8a521a9a4c80aee7444a8a7178bf36b6a126b1ea975117fc7b204

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.21@sha256:2c29f46a1b56f33364ad5375639526a121bc8dfdefc89a901d3d7992b110c877

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
