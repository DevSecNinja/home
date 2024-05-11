# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.48@sha256:d0fcf8c8691df20fe1a280d0a4cbc8493b04c7bd8cf8ca56264279510f030e49

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** pedantic/unbound:latest@sha256:78e52f968b1000c66eb4da7df74ec4b86951a91c1c341f10843cf774d89a1e35

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

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.4.1-beta@sha256:df07fd1315f077412cb1844d31ac9b89152102b8bcb0b7345de82bcb3406795f

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.3.2@sha256:f0a6faee9d0e55492f238d1d11ff13d77616ea12d8c38bedf090da2ee05532be

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor:v0.49.1@sha256:3cde6faf0791ebf7b41d6f8ae7145466fed712ea6f252c935294d2608b1af388

**url:** cadvisor-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.45.22@sha256:3669b2c8464f5914ed05d76290d6401b4946c2cfbaa7621dda9d02b0f5b63c3a

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

**image:** lscr.io/linuxserver/code-server:4.23.1@sha256:6852d23614cdc2cf4f03d22445cd5eb134f2a7137b9bedc20f60bc4b83c687d5

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.18.3@sha256:248f5276c1917980e725a48770fc50d4ea8d208383cb61e4da019020a11ce361

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v6.5.2@sha256:3669c8ffe32b1436db0a879ef32750ba83c8b9134062835d1b7b54c1f6c0ba6f

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:b17c7ab910add1ffdb18a700dceb19b8d23edf99c7bbe5fef32a5a593b610ae5

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:24.3.1@sha256:c6e4f6e1165922195e38f262bb59300257c92667d864de0649382464ffe108b7

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:33@sha256:17f45542b4442474f4b68bf6e97f9a321b2c0fe95c5126c429fe49d911b07eb3

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:bbb83fa30f5f8528126d37bf9c054318733579836aa30874ac28e3c0ec62550b

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:7.6.21@sha256:6008d7c213c19ea98cb5c3af26ab11b924b3a280e332571d8853c289c45dde14

**url:** folding-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.10.0@sha256:881131a4c74bc8a83c09dc4eb83ef659885d5caf84baabdfcc94fcc13f9e39f6

**url:** uptime.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.2-alpine@sha256:951bfda460300925caa3949eaa092ba022e9aec191bbea9056a39e2382260b27

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

**container_name:** grafana

**image:** grafana/grafana:10.4.2@sha256:7d5faae481a4c6f436c99e98af11534f7fd5e8d3e35213552dd1dd02bc393d2e

**url:** grafana.$DOMAINNAME

### Service: loki

**container_name:** loki

**image:** grafana/loki:3.0.0@sha256:757b5fadf816a1396f1fea598152947421fa49cb8b2db1ddd2a6e30fae003253

**url:** loki.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.8.12@sha256:ad5a8edea1c25b50c6d180d35f72c1623986335113457c4ba38e1ddf16816a4b

**url:** homepage-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:b17c7ab910add1ffdb18a700dceb19b8d23edf99c7bbe5fef32a5a593b610ae5

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

**container_name:** influxdb

**image:** influxdb:2.7.5-alpine@sha256:fffdcab19393a354155d33f2eec1fca1e35c70989f6a804ecc9fa66e4919cfe6

**url:** influxdb-noauth.$DOMAINNAME

### Service: influxdb-backup

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

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

**image:** docker.io/library/postgres:16.2-alpine@sha256:951bfda460300925caa3949eaa092ba022e9aec191bbea9056a39e2382260b27

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v0.153.1@sha256:e6e198779e7dec03aec5c9d846a0c284e99f5e51bf21c69ba5baa19d3eaf2015

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

**container_name:** mailrise

**image:** yoryan/mailrise:1.4.0@sha256:66082168090b9a83f01cc71a9d7b1994840adbbbffbe4d2cf644272fbbc23a1a

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:29.0.0-apache@sha256:a03b4456626f6c3c8e928961f4681bb42fcc6e4ce30dc5de7d3bf78af678d76b

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:29.0.0-apache@sha256:a03b4456626f6c3c8e928961f4681bb42fcc6e4ce30dc5de7d3bf78af678d76b

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.3.2@sha256:f0a6faee9d0e55492f238d1d11ff13d77616ea12d8c38bedf090da2ee05532be

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:3487aa5cf06dceb38202b06bba45b6e6d8a92288848698a6518eee5f63a293a3

## docker/ansible/templates/compose-modules/nodeexporter.yml

### Service: nodeexporter

**container_name:** nodeexporter

**image:** prom/node-exporter:v1.8.0@sha256:8a57af80a4c77ffb97749b44895248563616fcfd405b5370d5db35fe6c15e4ec

**url:** nodeexporter-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/oauth2-proxy.yml

### Service: oauth2_proxy

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy

**image:** bitnami/oauth2-proxy

### Service: oauth2_proxy_redis

> :warning: **Deprecation Notice:** Replaced by: Traefik Forward Auth with Entra ID authentication

**container_name:** oauth2-proxy-redis

**image:** redis:alpine3.19@sha256:3487aa5cf06dceb38202b06bba45b6e6d8a92288848698a6518eee5f63a293a3

## docker/ansible/templates/compose-modules/openspeedtest.yml

### Service: openspeedtest

**container_name:** openspeedtest

**image:** openspeedtest/latest:v2.0.5@sha256:bbddd8eda80cc4deb2a5702efd0acd826137650ba0bfcc6720f896c74bca02ee

**url:** speedtest.$DOMAINNAME

## docker/ansible/templates/compose-modules/paperless-ngx.yml

### Service: paperless-db

**container_name:** paperless-db

**image:** docker.io/library/postgres:16.2-alpine@sha256:951bfda460300925caa3949eaa092ba022e9aec191bbea9056a39e2382260b27

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.5.0@sha256:d1737c98b2a39e656cceac67126a4a82ff3c0e572beb3aa8a17d04a41d9eed17

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:3487aa5cf06dceb38202b06bba45b6e6d8a92288848698a6518eee5f63a293a3

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:20db3df89eaeb1b271dd840888fe909b88b12f4b86ef641ec07a1d45d4c5168f

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.7.2@sha256:703c990a790dfd4d25fb56df3afec27b13cb0926a3818bf265edac9c71311647

**url:** paperless.$DOMAINNAME

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

**url:** papermerge.$DOMAINNAME

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

**container_name:** photoprism

**image:** photoprism/photoprism:preview@sha256:b914356c3d138f2a687a84e06f729bc7b2c0756a1ca1b7c7b418e397a0f863ee

**url:** photos.$DOMAINNAME

### Service: photoprism-db

**container_name:** photoprism-db

**image:** mariadb:11.3.2@sha256:f0a6faee9d0e55492f238d1d11ff13d77616ea12d8c38bedf090da2ee05532be

### Service: photoprism-db-backup

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:57de6b3d028cb77bca69523ab2f65a61b23d40db5f4c1c1163b7b16dc29e6a3d

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** ghcr.io/linuxserver/plex:1.40.2@sha256:efcde01a7f245a419797cc77e343a8b36af1377cf5d397fead81de8099bdeb7b

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.20.2-alpine@sha256:d35be15c11e1491bf1f3c8b4a634769c5864c3ddef75287e98692a37afc6a093

**url:** portainer-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:b17c7ab910add1ffdb18a700dceb19b8d23edf99c7bbe5fef32a5a593b610ae5

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

**container_name:** prometheus

**image:** prom/prometheus:v2.51.2@sha256:4f6c47e39a9064028766e8c95890ed15690c30f00c4ba14e7ce6ae1ded0295b1

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

**image:** lscr.io/linuxserver/socket-proxy:1.24.0@sha256:b17c7ab910add1ffdb18a700dceb19b8d23edf99c7bbe5fef32a5a593b610ae5

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

**image:** linuxserver/unifi-network-application:8.1.127@sha256:90b58e91776b44d82f0bea3d8c0c824abdfedc8358822c15c0de2dcfe317cb5e

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.9@sha256:c578cda6630625bee0f7c522120fd89a8ffc2b9d88fa77a6ceb3447cedbd412a

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

**image:** hashicorp/vault:1.16@sha256:e139ff28c23e1f22a6e325696318141259b177097d8e238a3a4c5b84862fadd8

**url:** vault.$DOMAINNAME`) && PathPrefix(`/v1

## docker/ansible/templates/compose-modules/vikunja.yml

### Service: vikunja

**container_name:** vikunja

**image:** vikunja/vikunja:0.23.0@sha256:c824f99b0b09b7f03a1d77ad6691fbce38edf8d737e73e3242d8b87dd96d21e0

**url:** vikunja.$DOMAINNAME

### Service: vikunja-db

**container_name:** vikunja-db

**image:** mariadb:11.3.2@sha256:f0a6faee9d0e55492f238d1d11ff13d77616ea12d8c38bedf090da2ee05532be

### Service: vikunja-db-backup

**container_name:** vikunja-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

## docker/ansible/templates/compose-modules/wallabag.yml

### Service: wallabag

**container_name:** wallabag

**image:** wallabag/wallabag:2.6.9@sha256:d482b139bab164afef0e8bbfbeb7c55cd3e10e848b95d7d167e4ffcbc847f4b9

**url:** wallabag.$DOMAINNAME

### Service: wallabag-db

**container_name:** wallabag-db

**image:** mariadb:11.3.2@sha256:f0a6faee9d0e55492f238d1d11ff13d77616ea12d8c38bedf090da2ee05532be

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.0.35@sha256:794ffd160cf01057d0f64ef7baf5da3cd8925a48f1f65653e016f58c7d69b13c

### Service: wallabag-redis

**container_name:** wallabag-redis

**image:** redis:alpine3.19@sha256:3487aa5cf06dceb38202b06bba45b6e6d8a92288848698a6518eee5f63a293a3

## docker/ansible/templates/compose-modules/watchtower.yml

### Service: watchtower

> :warning: **Deprecation Notice:** Replaced by: Renovate Bot, GitHub Pull Requests and tags on the image

**container_name:** watchtower

**image:** containrrr/watchtower

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:1.0.20210914@sha256:a0e39a201018b0e990e82445ab7b2098cd25b1b7601ddcb8c50f2bb517da39d5

**url:** wireguard.$DOMAINNAME
