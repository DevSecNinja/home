# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.54@sha256:ec59d9d8d083b74620f827879bee7ad88621f96bc0c4347c84c176ffa349484c

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.22.0@sha256:76906da36d1806f3387338f15dcf8b357c51ce6897fb6450d6ce010460927e90

## docker/ansible/templates/compose-modules/alertmanager.yml

### Service: alertmanager

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** alertmanager

**image:** prom/alertmanager

## docker/ansible/templates/compose-modules/authelia.yml

### Service: authelia

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia

**image:** authelia/authelia

### Service: authelia-db-backup

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.10.2-beta@sha256:f3e31a3f8e4d3998ca6409ec81ebe2dc0bcc44c51d9985fa6e285514aae96cd8

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.5.2@sha256:4a1de8fa2a929944373d7421105500ff6f889ce90dcb883fbb2fdb070e4d427e

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.47.06@sha256:6e9dcf4abc1cfb0b1eeba6b6ff52a4b6f790110d6cdc8b7942c6cecf34e56265

**url:** change-detection.$DOMAINNAME

## docker/ansible/templates/compose-modules/cloudflare-companion.yml

### Service: cloudflare-companion

**container_name:** cloudflare-companion

**image:** tiredofit/traefik-cloudflare-companion:7.3.2@sha256:716a265a69f5f75ddbb089c19fe8e4b52cfd891f1dd426fe0e525a3ddf941ac8

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.15.0@sha256:d5649aee7c9e8f7e14a6efd5f2aa0db78ff5eee597da4dc78d950cbf6131bef8

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

**image:** amir20/dozzle:v8.7.3@sha256:7234eadb844a0454bee8d2596b20f15c7803b6813b04eefddf82ea42f1da1281

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:24.7.17@sha256:3e14dbd7818bb2222ef93d920809771dbbdc1bf8e1d8794c99314ad9a922eeb6

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:35@sha256:440ca6b810bc04606aac700e461caca5543eaa882c4e0af96a33424d05a23592

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:4d5423c1d80f353458307324b169500df334856eccc2e39fc6fa13808a64e1c2

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:ea935e320dc0eac34007f8632c471557cdb938ac3fa3f138a715123ab5cddc26

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.13.1@sha256:977129a3cad3253906ef9c95d16a0f19a3ab5d3892404da809798b5b34bbd04d

**url:** status-docker.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** grafana

**image:** grafana/grafana

### Service: loki

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** loki

**image:** grafana/loki

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:c7f8797b241c097df89145f9d8beca21c2ddc3bb3945dfb426bff654b11f4bfc

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.9.11@sha256:d41dca72f3a68d2c675eb232a448104af200096f05e2610ffbfdb16bc7f71410

**url:** homepage-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.10.1@sha256:87197b41262f8c23a57136d3848954d244d7d716a189c05bc4b9738c09bee535

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** influxdb

**image:** influxdb

### Service: influxdb-backup

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

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

**image:** sissbruecker/linkding:1.36.0-alpine@sha256:137dd201797c186419c92c32f0c42c61bdb85f60653932c96985a0e6995a4286

**url:** linkding.$DOMAINNAME

### Service: linkding-db

**container_name:** linkding-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v1.29.6@sha256:afebfaaeb516f502e64b21019531525aca58f28a777c95463c297b2ec1f177b2

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** mailrise

**image:** yoryan/mailrise

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.67.1@sha256:ee4ef2c8a4439ca01efe60d7c56cd678facdce2b411a1e338bd446e6deb8e061

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:30.0.2-apache@sha256:300c55b0ebe11991c61a346025791ea5ebd90a14cec4abc6048aab2f1baaf69c

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:30.0.2-apache@sha256:300c55b0ebe11991c61a346025791ea5ebd90a14cec4abc6048aab2f1baaf69c

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.5.2@sha256:4a1de8fa2a929944373d7421105500ff6f889ce90dcb883fbb2fdb070e4d427e

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/nodeexporter.yml

### Service: nodeexporter

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** nodeexporter

**image:** prom/node-exporter

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

## docker/ansible/templates/compose-modules/outline.yml

### Service: outline

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment

**container_name:** outline

**image:** outlinewiki/outline

### Service: outline-db

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment

**container_name:** outline-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: outline-db-backup

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment

**container_name:** outline-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

### Service: outline-redis

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment

**container_name:** outline-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/paperless-ngx.yml

### Service: paperless-db

**container_name:** paperless-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:5660c2cbfea50c7a9127d17dc4e48543eedd3d7a41a595a2dfa572471e37e64c

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.13.0@sha256:1917c80269a30d53979f8354bce6aabb8a2a62a38f727362c394edfbceaa7640

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:20db3df89eaeb1b271dd840888fe909b88b12f4b86ef641ec07a1d45d4c5168f

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.13.5@sha256:199c67ed55bfb9d58bf90db2ee280880ae9ebc63413e54c73522f9c4ebdc7bad

**url:** paperless.$DOMAINNAME

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

**url:** papermerge.$DOMAINNAME

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment of Immich

**container_name:** photoprism

**image:** photoprism/photoprism

### Service: photoprism-db

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment of Immich

**container_name:** photoprism-db

**image:** mariadb

### Service: photoprism-db-backup

> :warning: **Deprecation Notice:** Replaced by: Kubernetes deployment of Immich

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:4c1653fac64f6562f52c718c366ebcd2f0537585f70cda0014399d47bf920b5f

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.1.9057-af5eaea7a@sha256:8e4e0c2348eed53aed2ee7136dc58b733d5edd50dd0e65eeb2dc42eeb978bb0f

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.23.0-alpine@sha256:97342cf8a821d64d59880bdede8f45ea9c869fea702dd56128a67d552dc632ab

**url:** portainer-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** prometheus

**image:** prom/prometheus

### Service: pushgateway

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** pushgateway

**image:** prom/pushgateway

## docker/ansible/templates/compose-modules/promtail.yml

### Service: promtail

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** promtail

**image:** grafana/promtail

### Service: promtail-docker-proxy

> :warning: **Deprecation Notice:** Replaced by: Kubernetes cluster resource

**container_name:** promtail-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

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

**image:** ghcr.io/italypaleale/traefik-forward-auth:3.1.5@sha256:fc717ff42f367f5bc5f0101880cd488d46acd56c7fd3a6094c78a414e58c183d

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-8.4.62@sha256:694bd1e3b06b3f180ccc5cc052f8893ff450484a16e32cef7569565656235f59

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.15@sha256:8ff7333c6a9fbc00597fcce4c836e8bcc6b29fd34d49259479c43174e32d72be

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

## docker/ansible/templates/compose-modules/uptime-kuma.yml

### Service: uptime-kuma

> :warning: **Deprecation Notice:** Replaced by: Gatus

**container_name:** uptime-kuma

**image:** louislam/uptime-kuma

## docker/ansible/templates/compose-modules/vault.yml

### Service: vault

**container_name:** vault

**image:** hashicorp/vault:1.18@sha256:3580fa352195aa7e76449cb8fadeef6d2f90a454c38982d30cf094e9013be786

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

**image:** wallabag/wallabag:2.6.10@sha256:8854765d299d8e93f962d4be02ceb5703ed2ee24ec6c884f870bb7a18de41378

**url:** wallabag.$DOMAINNAME

### Service: wallabag-db

**container_name:** wallabag-db

**image:** mariadb:11.5.2@sha256:4a1de8fa2a929944373d7421105500ff6f889ce90dcb883fbb2fdb070e4d427e

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.1.9@sha256:0b2d0dee38fbe5dbffd63df59afc2b812d36f31ff1213a0f45f7e8901ac9de87

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

**image:** benbusby/whoogle-search:latest@sha256:60e071aa7c8b8d486c9bca773e26688744ca22cfdb61f58fa6a7f41fc50cd848

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
