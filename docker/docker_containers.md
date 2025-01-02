# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.55@sha256:2979cc78a28aceb77f90980a5440578dbb7bc406dffe261e9ae402750193bde0

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/beaverhabits.yml

### Service: beaverhabits

**container_name:** beaverhabits

**image:** daya0576/beaverhabits:0.4@sha256:e7bec8d18e149c3b19973cd178639b0b5f05450265cc4e2bba4e0581937adaae

**url:** habits.$DOMAINNAME

### Service: beaverhabits-db-backup

**container_name:** beaverhabits-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.12.1-beta@sha256:c67cb999aea3d147d7e491c9cc908d8a480faa13f2e04fc61b32c96481162a01

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.6.2@sha256:a9547599cd87d7242435aea6fda22a9d83e2c06d16c658ef70d2868b3d3f6a80

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.15.1@sha256:a4e2089b3531eec8c9328c7a9a586f80e8d67dcd94856e0b596b7896e1de3f62

## docker/ansible/templates/compose-modules/code-server.yml

### Service: code-server

**container_name:** code-server

**image:** lscr.io/linuxserver/code-server:version-4.89.0@sha256:678e01467fecf0d1d32b938f3f5324a69f74f9187d37fadddb8f926024524b8b

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.19.4@sha256:a2bfe382b2547bdd0a3d0523b9a6b85fab833c56bcec86d600ba6266910b533e

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v8.9.0@sha256:290837c69e70f6a38a0414cfd810b70211f08d41cc243189e6151dc07bc450bc

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:46992e6a45e09cec882760aa40f58912fb6ff3b9c1eb1a333e6380a68a232ce8

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:26.0.2@sha256:1a51e927bd75abb82e93a4151e4a1cfac06c5d622f92c2ad4672850267664287

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:35@sha256:440ca6b810bc04606aac700e461caca5543eaa882c4e0af96a33424d05a23592

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:56163a0c3eaeaf3444b3addf60d7cb6011a56bd17a7d0e1c24f11e62324a5d07

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.15.0@sha256:244af66f5eacb50040c2f1178913aecb301fc5bcd25720d99f89ec4a65964ecc

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.6-alpine@sha256:91e75546b4f229fa92cec21a2bf831ba03a1c101fc197daafff657f153e93a39

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:4bf60f55e6682bd134574a91fd9a4820dd6970ed5c08b6c0b7b841e4288ecbaa

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.10.6@sha256:426d75031d40a47d58b962766a4d11277490973c137ff5a98e051c9d204f5268

**url:** apps-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:46992e6a45e09cec882760aa40f58912fb6ff3b9c1eb1a333e6380a68a232ce8

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.12.0@sha256:4119b155dc2fb8cb088ef427e16b955339d02f9a8587e577dcb6812d9f31d890

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.6-alpine@sha256:91e75546b4f229fa92cec21a2bf831ba03a1c101fc197daafff657f153e93a39

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v1.42.4@sha256:6ce57a7f86d4ad591635e19a6e7f3a02bdeef65c55065a7f722f72dc02485705

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.73.1@sha256:9caf109e2293557568ab687b9d6c82646250c8ab7dcb20479c8bef9956811b7a

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.6-alpine@sha256:91e75546b4f229fa92cec21a2bf831ba03a1c101fc197daafff657f153e93a39

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:30.0.4-apache@sha256:6bba95a59b3bcc95b81c93b8fc5299ad2ea8d83692e6cf289650c132f7151209

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:30.0.4-apache@sha256:6bba95a59b3bcc95b81c93b8fc5299ad2ea8d83692e6cf289650c132f7151209

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.6.2@sha256:a9547599cd87d7242435aea6fda22a9d83e2c06d16c658ef70d2868b3d3f6a80

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.5@sha256:bbddd8eda80cc4deb2a5702efd0acd826137650ba0bfcc6720f896c74bca02ee

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:e2306dbeddb7901fb3f08bb0c8e5896ef816e8d53f6bdd82ffb538e5fc5a725e

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.3.9314-a0bfb8370@sha256:3d2ed27abb4f72038705c3e0c3d40ff89821a0c66d43e55125873de127197d25

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.1.5@sha256:fc717ff42f367f5bc5f0101880cd488d46acd56c7fd3a6094c78a414e58c183d

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-8.4.62@sha256:694bd1e3b06b3f180ccc5cc052f8893ff450484a16e32cef7569565656235f59

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.16@sha256:725b4cfe87014950ce9b423ac0a03035f6014a33475030403a3e583eb1485045

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/whoogle.yml

### Service: whoogle

**container_name:** whoogle

**image:** benbusby/whoogle-search:latest@sha256:60e071aa7c8b8d486c9bca773e26688744ca22cfdb61f58fa6a7f41fc50cd848

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
