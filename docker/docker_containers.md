# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.48@sha256:d0fcf8c8691df20fe1a280d0a4cbc8493b04c7bd8cf8ca56264279510f030e49

### Service: unbound

**container_name:** unbound

**image:** pedantic/unbound:latest@sha256:4396fa6330d19e4ed56d7ac14b40cec0d767bb0c47fa0ed37d30d973db01a5ae

## docker/ansible/templates/compose-modules/alertmanager.yml

### Service: alertmanager

**container_name:** alertmanager

**image:** prom/alertmanager:v0.27.0@sha256:45c3a586d4332d710bef92b06e90380c0b1f588968c00100d4b5e4e44c40ca5f

## docker/ansible/templates/compose-modules/authelia.yml

### Service: authelia

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia

**image:** authelia/authelia

### Service: authelia-db-backup

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** authelia-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.4.1-beta@sha256:df07fd1315f077412cb1844d31ac9b89152102b8bcb0b7345de82bcb3406795f

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.3.2@sha256:851f05fe1e4cb290442c1b12b7108436a33fd8f6a733d4989950322d06d45c65

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor:v0.49.1@sha256:3cde6faf0791ebf7b41d6f8ae7145466fed712ea6f252c935294d2608b1af388

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.45.21@sha256:6e80b83184b07fa8ac1d2ab42c5fca1620cedf7000fbb6db2c2de6d8babf203c

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

**image:** lscr.io/linuxserver/code-server:4.23.0@sha256:83f9360098a7b72592969807d5003df64fcf2ba07bb09b8fd19be68aac101636

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v6.5.1@sha256:bf8e7d302d2967c28e923f178b0926a747c5060d5014f38bc7676bf0cf0c226b

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:093b8b0bc4222ea246a56ff905212fd499f5434b85ddc37aca8d912de17454ac

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:24.2.2@sha256:ab82dbb4bf75e355b047d55ecd749d9d51271159979e8ee0fc120bffbc31cb2c

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:33@sha256:17f45542b4442474f4b68bf6e97f9a321b2c0fe95c5126c429fe49d911b07eb3

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:648edf36c55793fdeed475e09a86fb6c16a68783dc442d37d5070adfc0362a8f

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:7.6.21@sha256:6daaa802414b4330004f7d0b24f9394d55835c625727782c4239fd8ebcef9d9b

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.10.0@sha256:881131a4c74bc8a83c09dc4eb83ef659885d5caf84baabdfcc94fcc13f9e39f6

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.2-alpine@sha256:b89a4e92591810eac1fbce6107485d7c6b9449df51c1ccfcfed514a7fdd69955

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

**container_name:** grafana

**image:** grafana/grafana:10.4.1@sha256:753bbb971071480d6630d3aa0d55345188c02f39456664f67c1ea443593638d0

### Service: loki

**container_name:** loki

**image:** grafana/loki:3.0.0@sha256:451563d761403fd66fdf7abef934f8712e864d47ef88f7b64e8ca52852fdaf28

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.8.12@sha256:ad5a8edea1c25b50c6d180d35f72c1623986335113457c4ba38e1ddf16816a4b

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:093b8b0bc4222ea246a56ff905212fd499f5434b85ddc37aca8d912de17454ac

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

**container_name:** influxdb

**image:** influxdb:2.7.5-alpine@sha256:fffdcab19393a354155d33f2eec1fca1e35c70989f6a804ecc9fa66e4919cfe6

### Service: influxdb-backup

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/jupyter.yml

### Service: jupyter

**container_name:** jupyter

**image:** quay.io/jupyter/scipy-notebook:2024-03-14@sha256:1a6638b2861bae9bf8ec2fc9df30f3c1a5b3ee60a52ff0bffb637e0898effb55

## docker/ansible/templates/compose-modules/linkding.yml

### Service: linkding

**container_name:** linkding

**image:** sissbruecker/linkding:1.30.0-alpine@sha256:ad14934dc4c638a9564122678d2298e128065e4b8e5ae113785aa1edbddb4248

### Service: linkding-db

**container_name:** linkding-db

**image:** docker.io/library/postgres:16.2-alpine@sha256:b89a4e92591810eac1fbce6107485d7c6b9449df51c1ccfcfed514a7fdd69955

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

**container_name:** mailrise

**image:** yoryan/mailrise:1.4.0@sha256:66082168090b9a83f01cc71a9d7b1994840adbbbffbe4d2cf644272fbbc23a1a

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:28.0.4-apache@sha256:ee6e559f740416b8f34bd1dc8fc9a0f1c90d00800fdfba3b1d493e86ebecd5ae

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:28.0.4-apache@sha256:ee6e559f740416b8f34bd1dc8fc9a0f1c90d00800fdfba3b1d493e86ebecd5ae

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.3.2@sha256:851f05fe1e4cb290442c1b12b7108436a33fd8f6a733d4989950322d06d45c65

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:c1ac6782927e574394225a790b6eb476154d1a16681b1374c62625d9bc324b18

## docker/ansible/templates/compose-modules/nodeexporter.yml

### Service: nodeexporter

**container_name:** nodeexporter

**image:** prom/node-exporter:v1.7.0@sha256:4cb2b9019f1757be8482419002cb7afe028fdba35d47958829e4cfeaf6246d80

## docker/ansible/templates/compose-modules/oauth2-proxy.yml

### Service: oauth2_proxy

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy

**image:** bitnami/oauth2-proxy

### Service: oauth2_proxy_redis

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy-redis

**image:** redis:7.2.4-alpine@sha256:1b503bb77079ba644371969e06e1a6a1670bb34c2251107c0fc3a21ef9fdaeca

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.5@sha256:12cb104a9c10ee2b3a9ffcc1992dfb72236e8c2e3a08aa700f19b705fe3f2f04

## docker/ansible/templates/compose-modules/paperless-ngx.yml

### Service: paperless-db

**container_name:** paperless-db

**image:** docker.io/library/postgres:16.2-alpine@sha256:b89a4e92591810eac1fbce6107485d7c6b9449df51c1ccfcfed514a7fdd69955

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.4.0@sha256:97a566eb0c9d8c103e90dc21970f6e0d05c3e41fb96f2ac2b28cd92f956df398

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:c1ac6782927e574394225a790b6eb476154d1a16681b1374c62625d9bc324b18

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:8765f135f5c9d58d8a8fe56fdacc589aebaa812301d184c53e1aeb6e5a054145

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.7.0@sha256:93ed7056a2695fd3feb5408dfd8b2630d7ad6cb53446db5b212d3d7992c0761c

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

**container_name:** photoprism

**image:** photoprism/photoprism:preview@sha256:aa844a49c04e44e975a786bf2f7ce8d43ab71852f2b0d7375d7e27431aba909f

### Service: photoprism-db

**container_name:** photoprism-db

**image:** mariadb:11.3.2@sha256:851f05fe1e4cb290442c1b12b7108436a33fd8f6a733d4989950322d06d45c65

### Service: photoprism-db-backup

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:9d807f4126d5793e405a398b2f2327cd7a3548af99d8dd6a164969974d5975e7

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** ghcr.io/linuxserver/plex:1.40.1@sha256:e7274807e5366c06992e57ae55cc06916360c4817550fe8d22a0671711334cdb

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.20.1-alpine@sha256:78c026175e15203b8012518141291ad484f1c46d8cb94c67b389555169f27c19

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:093b8b0bc4222ea246a56ff905212fd499f5434b85ddc37aca8d912de17454ac

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

**container_name:** prometheus

**image:** prom/prometheus:v2.51.1@sha256:dec2018ae55885fed717f25c289b8c9cff0bf5fbb9e619fb49b6161ac493c016

### Service: pushgateway

**container_name:** pushgateway

**image:** prom/pushgateway:v1.8.0@sha256:c159e946abf44e0cf4ae53aa03d99326497a35acca526739c7f8b01a0183bb50

## docker/ansible/templates/compose-modules/promtail.yml

### Service: promtail

**container_name:** promtail

**image:** grafana/promtail:3.0.0@sha256:43c497a102e333c30b7c0f9a45d9107151f6424bd40c424d96791e65b6f2aeb0

### Service: promtail-docker-proxy

**container_name:** promtail-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:093b8b0bc4222ea246a56ff905212fd499f5434b85ddc37aca8d912de17454ac

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

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** linuxserver/unifi-network-application:8.1.113@sha256:6b551dc2f2290c45b8c358690114cf6f199053a53f2809a89af6b27255ca145f

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.8@sha256:5505a38a8c6044ace154376dfe4c94ac85f01c22585547efdd9483c4922dfa37

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/uptime-kuma.yml

### Service: uptime-kuma

> :warning: **Deprecation Notice:** Replaced by: Gatus

**container_name:** uptime-kuma

**image:** louislam/uptime-kuma

## docker/ansible/templates/compose-modules/vault.yml

### Service: vault

**container_name:** vault

**image:** hashicorp/vault:1.16@sha256:2e1b2d939a8a5362ebb28622aafc9d1e4c78e7ff5e66437e594bae9ddd0a6789

## docker/ansible/templates/compose-modules/vikunja.yml

### Service: vikunja

**container_name:** vikunja

**image:** vikunja/vikunja:0.23.0@sha256:8756e990c4cd842c981f586ab26f543ecdfc5c925b1b3469118156d418c79550

### Service: vikunja-db

**container_name:** vikunja-db

**image:** mariadb:11.3.2@sha256:851f05fe1e4cb290442c1b12b7108436a33fd8f6a733d4989950322d06d45c65

### Service: vikunja-db-backup

**container_name:** vikunja-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/wallabag.yml

### Service: wallabag

**container_name:** wallabag

**image:** wallabag/wallabag:2.6.9@sha256:d482b139bab164afef0e8bbfbeb7c55cd3e10e848b95d7d167e4ffcbc847f4b9

### Service: wallabag-db

**container_name:** wallabag-db

**image:** mariadb:11.3.2@sha256:851f05fe1e4cb290442c1b12b7108436a33fd8f6a733d4989950322d06d45c65

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: wallabag-redis

**container_name:** wallabag-redis

**image:** redis:alpine3.19@sha256:c1ac6782927e574394225a790b6eb476154d1a16681b1374c62625d9bc324b18

## docker/ansible/templates/compose-modules/watchtower.yml

### Service: watchtower

> :warning: **Deprecation Notice:** Replaced by: Renovate Bot, GitHub Pull Requests and tags on the image

**container_name:** watchtower

**image:** containrrr/watchtower
