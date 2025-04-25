# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.61@sha256:a2085b04bbfc4759e68fa1d13d4e1558aede67c783c55820e036a95a36dd3ebf

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

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2025.2.1-beta@sha256:d8d510eb726e0c2d265cb1f46f5ee22f208851eef5976efbd27172f1871a570c

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.7.2@sha256:81e893032978c4bf8ad43710b7a979774ed90787fa32d199162148ce28fe3b76

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

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

**image:** amir20/dozzle:v8.12.12@sha256:ed63d87135f0059bb45be651b8c73de8ecca29ebc57096fd9b5f8ce049d0dcdf

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.3-r0@sha256:a85b8cd8c30833f3ef2aaa35bd0cbb5170e4afc65efd3c9aef3ba8224e8c1ad6

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:26.2.8@sha256:232749107d0714c29acfcc0345c67e0e53c47a613235bd01ffb1e387579c6434

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:36@sha256:43bdfe52abc5baed00706337efe26825c86360c6b9b74659a72a9aa2fca8bd55

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:7c6fe0cd7dc44260aa70f79df787ee7635a9f9585e0a7f1d8a6d1f4d9225a4db

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.17.0@sha256:a8c53f9e9f1a3876cd00e44a42c80fc984e118d5ba0bdbaf08980cb627d61512

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:ab6b0c93c6dd89db4e8982763c19ade14b3b1d06b02198ce2f999f40665ffce9

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.10.9@sha256:b6d732817572f9af99ec168b10641b8f7820f30cfa5a5cc5c68f1e291804bec8

**url:** apps-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.3-r0@sha256:a85b8cd8c30833f3ef2aaa35bd0cbb5170e4afc65efd3c9aef3ba8224e8c1ad6

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2025.3.2@sha256:cea441f54fd36585d903ad74a9a5f703cdba1efa916a0b745a6137da08e96c03

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:1.82.7@sha256:0db6910b10143d532b68351eff0d8c259560522fc03912082311798c99830ecf

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.90.1@sha256:2bfcd8f750a4df151149a1401c27f8a70e5fe77be62c99388631a00d9961d9f1

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:31.0.4-apache@sha256:dc6004218585aba9d086499cc5c92a0c18f55a9c0d94fc88362722679a5dbed4

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:31.0.4-apache@sha256:dc6004218585aba9d086499cc5c92a0c18f55a9c0d94fc88362722679a5dbed4

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.7.2@sha256:81e893032978c4bf8ad43710b7a979774ed90787fa32d199162148ce28fe3b76

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

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

**image:** phpmyadmin:5.2.2-apache@sha256:216747e3a6b7ef8714b79ece498090910c0353a01606c63fe06199a54069683c

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.6.9685-d301f511a@sha256:c799512e714ea3c5bf5d4589b56a16e29d56bcf8ecfbfc368245514fe6500171

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.5.1@sha256:02cd57e208b923d1d6978c66bd56e73d109a8a9d2926a15a5530cb938d7da911

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.0.114@sha256:08c141dc6ba08fe05db01306ab633ac0478ef8677a1f308ef73bc3342f6f02f1

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.19@sha256:e5aa36b2b88d39499567ee93a5accc6add94ddc2efd6bb2a5d51b8a84da63e98

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.17@sha256:c2e1ce1707083ad7edcc429ffc8cdf9ab744fbb992d4038f9f85930c0e50cf23

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
