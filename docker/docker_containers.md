# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.50@sha256:f890b77505e410e295cc96830632b46075d7263cef52c158f9331348c98e1228

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.19.3@sha256:2b19bdb4db8d6f9ebd39d060e1a0ea66f198e5c7272c8b711fd7835594014385

## docker/ansible/templates/compose-modules/alertmanager.yml

### Service: alertmanager

**container_name:** alertmanager

**image:** prom/alertmanager:v0.27.0@sha256:e13b6ed5cb929eeaee733479dce55e10eb3bc2e9c4586c705a4e8da41e5eacf5

**url:** alertmanager.$DOMAINNAME

## docker/ansible/templates/compose-modules/authelia.yml

### Service: authelia

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia

**image:** authelia/authelia

### Service: authelia-db-backup

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.5.0-beta@sha256:82dd3318e3483492364c09a27819f6c14753e9bb721a4d81cf9c624b99057407

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.4.2@sha256:934277de8883c061e32a21d01c64973b28272b441a3f797faf189c045a7c0a51

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor:v0.49.1@sha256:3cde6faf0791ebf7b41d6f8ae7145466fed712ea6f252c935294d2608b1af388

**url:** cadvisor-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.45.23@sha256:b1175272d6afdbbfc1e2b3317bf34c29978a7461d49b29d452e3e8f41036a7ec

**url:** change-detection.$DOMAINNAME

## docker/ansible/templates/compose-modules/cloudflare-companion.yml

### Service: cloudflare-companion

**container_name:** cloudflare-companion

**image:** tiredofit/traefik-cloudflare-companion:7.2.0@sha256:3cb8d8ea9c35a5ff58120261e16723650468835d25130a53326679a109084a24

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.11.0@sha256:d4bca5975591da91a9c69ca1123267974ad0d76b676e709c42efd2695fafe4de

## docker/ansible/templates/compose-modules/code-server.yml

### Service: code-server

**container_name:** code-server

**image:** lscr.io/linuxserver/code-server:version-4.89.0@sha256:678e01467fecf0d1d32b938f3f5324a69f74f9187d37fadddb8f926024524b8b

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.18.6@sha256:4de4eff8227b43506953085732531471ee87247ac487537e3e72de9614eb3dda

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v7.0.3@sha256:47d9598489918c212c02700ccfc8034a34a6484383e389f20e90cd15dbc68e3d

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:817fbd545647e8e78fa87c5eb004bd83f8b5fd5dc558b654f89d85e9639993f1

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:24.5.2@sha256:cb2f5d7257cd6de2070cc09f3a7ba48c6d4bda174ac5e2234d4b4e57395f82af

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:33@sha256:17f45542b4442474f4b68bf6e97f9a321b2c0fe95c5126c429fe49d911b07eb3

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:d074f693cd8c417719c0370b637e1b7351814f9050e7b2ac62727c8071e3bf25

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-7.6.21@sha256:67bd2ec9c964f611ac3914575146d687bb320b6b1e2931f62e84e0d83676239e

**url:** folding-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.11.0@sha256:05cf8bcbd7296b2e47d9e69d5974d428dde32188722d2aa954367eb728dd056c

**url:** status.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:d037653693c4168efbb95cdc1db705d31278a4a8d608d133eca1f07af9793960

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

**container_name:** grafana

**image:** grafana/grafana:11.0.0@sha256:0dc5a246ab16bb2c38a349fb588174e832b4c6c2db0981d0c3e6cd774ba66a54

**url:** grafana.$DOMAINNAME

### Service: loki

**container_name:** loki

**image:** grafana/loki:3.0.0@sha256:757b5fadf816a1396f1fea598152947421fa49cb8b2db1ddd2a6e30fae003253

**url:** loki.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.9.2@sha256:5356c97b51e3cc817bed93612b4e57b39d28048ab9e4e3b346e827160cf0923e

**url:** homepage-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:817fbd545647e8e78fa87c5eb004bd83f8b5fd5dc558b654f89d85e9639993f1

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.3.3@sha256:e3cb8ae1edbf5d48a8e6126ab4b997c26f2559f930544fdb01a0b3b8c08c7a5d

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:d037653693c4168efbb95cdc1db705d31278a4a8d608d133eca1f07af9793960

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

**container_name:** influxdb

**image:** influxdb:2.7-alpine@sha256:8d8eae9bc4eb5db7c4ef41fb1ae3fa03ff8e9bb52d73f36f4c738758a50d54aa

**url:** influxdb-noauth.$DOMAINNAME

### Service: influxdb-backup

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/it-tools.yml

### Service: it-tools

**container_name:** it-tools

**image:** ghcr.io/corentinth/it-tools:2023.12.21-5ed3693@sha256:4aaf67eab769afc9dac5614a15614537446e11150d53eab3be34ac9775a27e3a

**url:** tools.$DOMAINNAME

## docker/ansible/templates/compose-modules/jupyter.yml

### Service: jupyter

> :warning: **Deprecation Notice:** Replaced by: nothing

**container_name:** jupyter

**image:** quay.io/jupyter/scipy-notebook

## docker/ansible/templates/compose-modules/linkding.yml

### Service: linkding

**container_name:** linkding

**image:** sissbruecker/linkding:1.30.0-alpine@sha256:ad14934dc4c638a9564122678d2298e128065e4b8e5ae113785aa1edbddb4248

**url:** linkding.$DOMAINNAME

### Service: linkding-db

**container_name:** linkding-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:d037653693c4168efbb95cdc1db705d31278a4a8d608d133eca1f07af9793960

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v0.162.19@sha256:f6ca1bce48f027d8a5d8d07e5ca7db78f10f698b44d07bb9a19809013ae33e05

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

**container_name:** mailrise

**image:** yoryan/mailrise:1.4.0@sha256:66082168090b9a83f01cc71a9d7b1994840adbbbffbe4d2cf644272fbbc23a1a

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:29.0.1-apache@sha256:4d966a5f80f044a47b6862825fce3d7822b2ad761e49b9269a70e56a0fd7a17c

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:29.0.1-apache@sha256:4d966a5f80f044a47b6862825fce3d7822b2ad761e49b9269a70e56a0fd7a17c

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.4.2@sha256:934277de8883c061e32a21d01c64973b28272b441a3f797faf189c045a7c0a51

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/nodeexporter.yml

### Service: nodeexporter

**container_name:** nodeexporter

**image:** prom/node-exporter:v1.8.1@sha256:fa7fa12a57eff607176d5c363d8bb08dfbf636b36ac3cb5613a202f3c61a6631

**url:** nodeexporter-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/oauth2-proxy.yml

### Service: oauth2_proxy

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy

**image:** bitnami/oauth2-proxy

### Service: oauth2_proxy_redis

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.5@sha256:bbddd8eda80cc4deb2a5702efd0acd826137650ba0bfcc6720f896c74bca02ee

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/paperless-ngx.yml

### Service: paperless-db

**container_name:** paperless-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:d037653693c4168efbb95cdc1db705d31278a4a8d608d133eca1f07af9793960

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.5.1@sha256:c229bd7a6c16800e9feabd102aacc445bd7c434d3a72e8df3cca6661314a0a3c

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:20db3df89eaeb1b271dd840888fe909b88b12f4b86ef641ec07a1d45d4c5168f

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.9.0@sha256:948dc7297df8259bffac23e564a7ca688bfc8f04fed9113e7fb14f6030da63dd

**url:** paperless.$DOMAINNAME

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

**url:** papermerge.$DOMAINNAME

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

**container_name:** photoprism

**image:** photoprism/photoprism:preview@sha256:67c1da51c1f1e3e4bbc50a370016cb04901f5f4ae25585f2eb007e1763f32126

**url:** photos.$DOMAINNAME

### Service: photoprism-db

**container_name:** photoprism-db

**image:** mariadb:11.4.2@sha256:934277de8883c061e32a21d01c64973b28272b441a3f797faf189c045a7c0a51

### Service: photoprism-db-backup

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:512a596a35a2b2865e3d710e5349f930165d40dac97e0e7a5129a6807c599ab2

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.40.2.8395-c67dce28e@sha256:addec5e26fb63af661992e0c50e0bd6f7a271433cd2a058f130e0ec1bae415e4

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.20.3-alpine@sha256:a6f635877e0daa4aa39c1cbf4e73a31b35d342284588fa72fd8a91efb3c6a091

**url:** portainer-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:817fbd545647e8e78fa87c5eb004bd83f8b5fd5dc558b654f89d85e9639993f1

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

**container_name:** prometheus

**image:** prom/prometheus:v2.52.0@sha256:5c435642ca4d8427ca26f4901c11114023004709037880cd7860d5b7176aa731

**url:** prometheus.$DOMAINNAME

### Service: pushgateway

**container_name:** pushgateway

**image:** prom/pushgateway:v1.8.0@sha256:c159e946abf44e0cf4ae53aa03d99326497a35acca526739c7f8b01a0183bb50

**url:** pushgateway.$DOMAINNAME

## docker/ansible/templates/compose-modules/promtail.yml

### Service: promtail

**container_name:** promtail

**image:** grafana/promtail:3.0.0@sha256:d3de3da9431cfbe74a6a94555050df5257f357e827be8e63f8998d509c37af8b

**url:** promtail.$DOMAINNAME

### Service: promtail-docker-proxy

**container_name:** promtail-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:817fbd545647e8e78fa87c5eb004bd83f8b5fd5dc558b654f89d85e9639993f1

## docker/ansible/templates/compose-modules/samba.yml

### Service: samba

> :warning: **Deprecation Notice:** Replaced by: Samba on VM with Ansible role vladgh.samba

**container_name:** samba

**image:** dperson/samba

## docker/ansible/templates/compose-modules/traefik-certs-dumper.yml

### Service: traefik-certs-dumper

> :warning: **Deprecation Notice:** Replaced by: none. Not needed anymore and was causing an extremely high CPU & I/O usage on Raspberry Pi (bug?)

**container_name:** traefik-certs-dumper

**image:** ldez/traefik-certs-dumper

## docker/ansible/templates/compose-modules/traefik-forward-auth.yml

### Service: traefik-forward-auth

**container_name:** traefik-forward-auth

**image:** ghcr.io/jordemort/traefik-forward-auth:latest@sha256:394f86bff5cc839fac1392f65dd3d4471e827bc29321a4460e7d92042e026599

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-8.2.93@sha256:d081c86593464a7c6f7acb9250377a46305b0c7d6b96dd8fd52e64d636a39250

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.11@sha256:bc16accb1a8ff9bbe44608ff82ac3a3a478c3a486f8b6f664281bbc489157f27

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

## docker/ansible/templates/compose-modules/uptime-kuma.yml

### Service: uptime-kuma

> :warning: **Deprecation Notice:** Replaced by: Gatus

**container_name:** uptime-kuma

**image:** louislam/uptime-kuma

## docker/ansible/templates/compose-modules/vault.yml

### Service: vault

**container_name:** vault

**image:** hashicorp/vault:1.16@sha256:c5e04689611cb864b8b6247a6a845e0bdc059998f39b5c8a659562287379525c

**url:** vault.$DOMAINNAME`) && PathPrefix(`/v1

## docker/ansible/templates/compose-modules/vikunja.yml

### Service: vikunja

> :warning: **Deprecation Notice:** Replaced by: nothing

**container_name:** vikunja

**image:** vikunja/vikunja

### Service: vikunja-db

> :warning: **Deprecation Notice:** Replaced by: nothing

**container_name:** vikunja-db

**image:** mariadb

### Service: vikunja-db-backup

> :warning: **Deprecation Notice:** Replaced by: nothing

**container_name:** vikunja-db-backup

**image:** tiredofit/db-backup

## docker/ansible/templates/compose-modules/wallabag.yml

### Service: wallabag

**container_name:** wallabag

**image:** wallabag/wallabag:2.6.9@sha256:d482b139bab164afef0e8bbfbeb7c55cd3e10e848b95d7d167e4ffcbc847f4b9

**url:** wallabag.$DOMAINNAME

### Service: wallabag-db

**container_name:** wallabag-db

**image:** mariadb:11.4.2@sha256:934277de8883c061e32a21d01c64973b28272b441a3f797faf189c045a7c0a51

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.1.0@sha256:39b45db5f4cfe5d5ed4764f8d8ce6c21e8e1bd9c05d27a733c34b78b765eef99

### Service: wallabag-redis

**container_name:** wallabag-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/watchtower.yml

### Service: watchtower

> :warning: **Deprecation Notice:** Replaced by: Renovate Bot, GitHub Pull Requests and tags on the image

**container_name:** watchtower

**image:** containrrr/watchtower

## docker/ansible/templates/compose-modules/whoogle.yml

### Service: whoogle

**container_name:** whoogle

**image:** benbusby/whoogle-search:latest@sha256:04e1aea20c6be99f0331671cb6dc3b09843fd3cc28b2bb4688603a4d8e4ec1d4

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
