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

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2025.1.0-beta@sha256:622dfe16bec7584f4a13d089f55438ad84eeebb08cc98d303a0ea5331c374cdd

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

**image:** amir20/dozzle:v8.10.4@sha256:25da7783d75db1a62a24b949cd54a9d2dc7791e63cf97099fa2d43e3f7b98a0e

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:46992e6a45e09cec882760aa40f58912fb6ff3b9c1eb1a333e6380a68a232ce8

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:26.0.6@sha256:d8a3a024f7f29b019d49bc92fba1f8288fb0a2b8467732f7b586351d1548f15d

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:35@sha256:440ca6b810bc04606aac700e461caca5543eaa882c4e0af96a33424d05a23592

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:49905be9d90ccf8d19986f6cfbfafc46c36c8a8ff6fbccad98f2032bb66a85d7

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

**image:** docker.io/library/postgres:16.6-alpine@sha256:aba1fab94626cf8b0f4549055214239a37e0a690f03f142b7bca05b9ed36c6db

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:df6d620d49b0d9be2edc92ac96c920b8495da161fd4d4d1b02b2876c54ab21cc

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.10.9@sha256:b6d732817572f9af99ec168b10641b8f7820f30cfa5a5cc5c68f1e291804bec8

**url:** apps-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:46992e6a45e09cec882760aa40f58912fb6ff3b9c1eb1a333e6380a68a232ce8

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.12.1@sha256:162e5d932c71c80dbea1d505930b3b903ca8b729e82d0fb2c149df59e590e500

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.6-alpine@sha256:aba1fab94626cf8b0f4549055214239a37e0a690f03f142b7bca05b9ed36c6db

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

**image:** lobehub/lobe-chat:v1.47.4@sha256:6f8faf6bb0060724da52d301d1c55eae57a75d7e345cf9eff14da539aa8164ed

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.75.2@sha256:6cf38471f4a368ba0d50dbec31bba0310a4e12565852619d79477953eb010e39

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.6-alpine@sha256:aba1fab94626cf8b0f4549055214239a37e0a690f03f142b7bca05b9ed36c6db

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:30.0.5-apache@sha256:02441f524c6fab3aadbf7157f6e0484927e231d685b248dc0734fa2941b4445e

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:30.0.5-apache@sha256:02441f524c6fab3aadbf7157f6e0484927e231d685b248dc0734fa2941b4445e

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

**image:** openspeedtest/latest:v2.0.6@sha256:a6a7e3b3e9e93cfe7b9b2eb49c60b2a93644149a0a600845d4df57148b193ff6

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:6e75aa8f767c5c9b7f3859e7f3006ad669739159d4e312e7570b66082da7f949

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.3.9314-a0bfb8370@sha256:dda062ebde8c619a656f7ed6e6da7885ca7e114536c1e76b1de3e32a57d3597b

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.1.5@sha256:fc717ff42f367f5bc5f0101880cd488d46acd56c7fd3a6094c78a414e58c183d

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.0.108@sha256:e6daac9a5cc9050e75864e17285df2e607a2082e81ab9b0186fc4946efd38761

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.16@sha256:24077ea3097e7b5dc5208354c62d607b1d08da6267b1c458d108cf77794b590c

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.12@sha256:d3ee1a8fe16200587bed037c81fb651db031d68f3809c38d8d62976aa0745e39

## docker/ansible/templates/compose-modules/whoogle.yml

### Service: whoogle

**container_name:** whoogle

**image:** benbusby/whoogle-search:latest@sha256:810bbb2f2e621bc13ed66498fa55a276c2aeee16a1a471c04d1672d405dad899

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
