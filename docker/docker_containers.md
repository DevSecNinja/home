# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.57@sha256:5c536c1e25f76693ae7ee5e64e8a029893e0f3f1778c8d2a9581383e60cfa9b9

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

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2025.2.1-beta@sha256:d8d510eb726e0c2d265cb1f46f5ee22f208851eef5976efbd27172f1871a570c

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.7.2@sha256:310d29fbb58169dcddb384b0ff138edb081e2773d6e2eceb976b3668089f2f84

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

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

**image:** amir20/dozzle:v8.11.9@sha256:b840926bc5f63be2296d3c99cf7c17a522d631b6afa7fce3fc744d65a1cb92f9

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:46992e6a45e09cec882760aa40f58912fb6ff3b9c1eb1a333e6380a68a232ce8

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:26.1.0@sha256:966e3d89915f95274ea835a92b6b03b5f55ea3f373d806aa0ca26d86ff94514b

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:35@sha256:440ca6b810bc04606aac700e461caca5543eaa882c4e0af96a33424d05a23592

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:0c95248ae1f3f582d7c4472504a963f52c4f2de4a8174a5b4a3d649e29ee31dc

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:a11530655be018bc43c9f973bce2a59344f2d140a9e5c843305f765299a5d141

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.16.0@sha256:bb738c87cf2e2a08b8fff180cfc433e7b8b87bb1779c1fb1b00f8b748673e3c3

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:f34de69aff7b21c7d7d474b86bef4dbce9613668b8d4a936e6c93b3844611505

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

**image:** hoppscotch/hoppscotch:2025.2.2@sha256:05c936b04dd9344dc85c3faa73866e0e756fec5942e5573d330f556c1efe7465

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:1.71.2@sha256:d42d1a347f5866a8dfae76fbf88446b77f4c2e9c3c3841514648e84ef0db07ea

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.83.2@sha256:5288543ac4dc1ea7149a93e38a24989c913c9007dd2459f6c730ac247c4d958f

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.8-alpine@sha256:3b057e1c2c6dfee60a30950096f3fab33be141dbb0fdd7af3d477083de94166c

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:31.0.1-apache@sha256:7ec3cf674ee868e3762a3bf913df56887e70a7b8dd1c7681fca6ef76233bd554

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:31.0.1-apache@sha256:7ec3cf674ee868e3762a3bf913df56887e70a7b8dd1c7681fca6ef76233bd554

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.7.2@sha256:310d29fbb58169dcddb384b0ff138edb081e2773d6e2eceb976b3668089f2f84

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

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

**image:** phpmyadmin:5.2.2-apache@sha256:97fa7d2bb353179c6c8484c09a59fd24ea3402cb16df63ab68c5e3b160c4becb

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.5.9522-a96edc606@sha256:535b88a993e3bfe7693edab81346817cd128794eb6fdae0eab02a953823d02f2

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.2.0@sha256:3942ad1e29b29592a7bc49272c8153d10afaa19d3d3dfbc1e0edfce15f48024a

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-9.0.114@sha256:79adf36ca9d19395b03fc3762c23478be3738fb9a62a3457b7456bc89ed60ccd

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.17@sha256:ac9e83c57e32bf767f875ac2b9a9d87800d2d91a7829180c3a4826e0599698e8

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.16@sha256:26541bb600bc817d9a69edd46141b03e6e6ff7612ac011f3a0264882f8435765

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
