# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.52@sha256:d16cc7517ab96f843e7f8bf8826402dba98f5e6b175858920296243332391589

**url:** adguard-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: unbound

**container_name:** unbound

**image:** mvance/unbound:1.20.0@sha256:4bf67b567f392956455bd4f8a4cdd48010e234f1a07c0a99c2cff2ddbb3e8a7a

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

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.6.2-beta@sha256:7ff2af1463b665e990d1cc12aa3e8f85fda9a7d9a69f38de0d9718e91d0c649e

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.4.2@sha256:e59ba8783bf7bc02a4779f103bb0d8751ac0e10f9471089709608377eded7aa8

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor:v0.49.1@sha256:3cde6faf0791ebf7b41d6f8ae7145466fed712ea6f252c935294d2608b1af388

**url:** cadvisor-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.45.26@sha256:85371f9997473f2bd3f5bec7a7344c1e2af73330bd4143902bed4d33e1c91a07

**url:** change-detection.$DOMAINNAME

## docker/ansible/templates/compose-modules/cloudflare-companion.yml

### Service: cloudflare-companion

**container_name:** cloudflare-companion

**image:** tiredofit/traefik-cloudflare-companion:7.3.1@sha256:c3aec9ff4f5ef5214678b6b72d299176a21c295664ff3297ac8b50fdd5788d76

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.12.0@sha256:436391bfe5584e366d901c18594bd033a4511bea5c98d0f8c0c460ad1eb7b4d2

## docker/ansible/templates/compose-modules/code-server.yml

### Service: code-server

**container_name:** code-server

**image:** lscr.io/linuxserver/code-server:version-4.89.0@sha256:678e01467fecf0d1d32b938f3f5324a69f74f9187d37fadddb8f926024524b8b

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.19.0@sha256:03edba99b2115e1ea6ca9aa6b58c84249c52d1369e5287335a167922617958da

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v8.0.5@sha256:df6eda9fbfa8944b757aa8ba8c77bc70c8f9f9458a9a6bfb83a771e38f25aa68

**url:** dozzle-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: dozzle-docker-proxy

**container_name:** dozzle-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:f66d1d802ad387f523ec89b7ae872c12396e4b996c0e21a1930e6a1d0b9205b4

## docker/ansible/templates/compose-modules/drawio.yml

### Service: drawio

**container_name:** drawio

**image:** jgraph/drawio:24.6.4@sha256:cbf7708fe5c908736c8fb3aca558e3ebdda0d77234de4c354427502247c0fd87

**url:** draw.$DOMAINNAME

## docker/ansible/templates/compose-modules/echo-server.yml

### Service: echo-server

**container_name:** echo-server

**image:** mendhak/http-https-echo:33@sha256:17f45542b4442474f4b68bf6e97f9a321b2c0fe95c5126c429fe49d911b07eb3

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:ad64c71819a7908fe9ec3686b630d8c443df69b7029a1faa8c667df4168acd64

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-7.6.21@sha256:9a997426d71e320f8d84429af148a4749e81def1cdf8f286d5135223d41f3bdd

**url:** folding-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.11.0@sha256:05cf8bcbd7296b2e47d9e69d5974d428dde32188722d2aa954367eb728dd056c

**url:** status.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:de3d7b6e4b5b3fe899e997579d6dfe95a99539d154abe03f0b6839133ed05065

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

**container_name:** grafana

**image:** grafana/grafana:11.1.0@sha256:079600c9517b678c10cda6006b4487d3174512fd4c6cface37df7822756ed7a5

**url:** grafana.$DOMAINNAME

### Service: loki

**container_name:** loki

**image:** grafana/loki:3.1.0@sha256:d947e68a84d9e44915dfa08c3bec27e2124efd5ba6c83443eb53578101ec69e3

**url:** loki.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.9.3@sha256:cbc5b49533f9afd0be57f6d5168eef48be2d713709259d6697f0d33b4ecb2f28

**url:** homepage-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:f66d1d802ad387f523ec89b7ae872c12396e4b996c0e21a1930e6a1d0b9205b4

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.6.0@sha256:e3a4c0e6fa1a92389308a853f2960cc9c2bc8d57817e9ad8261ac2721f07fb70

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:de3d7b6e4b5b3fe899e997579d6dfe95a99539d154abe03f0b6839133ed05065

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

**container_name:** influxdb

**image:** influxdb:2.7-alpine@sha256:b4ad0aa1e732e35d57cc4340c73e6c61d3f6cfc32b3c0163ca51d74f68acde4b

**url:** influxdb-noauth.$DOMAINNAME

### Service: influxdb-backup

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

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

**image:** sissbruecker/linkding:1.31.0-alpine@sha256:1fa14d3082148e8e6ac6c00e617bcb47c3a3f6cfc86e636a9c4a5a5c05dd493d

**url:** linkding.$DOMAINNAME

### Service: linkding-db

**container_name:** linkding-db

**image:** docker.io/library/postgres:16.3-alpine@sha256:de3d7b6e4b5b3fe899e997579d6dfe95a99539d154abe03f0b6839133ed05065

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v1.6.1@sha256:edc50cb8a8c7d593d1a69cad7e4b423b8f54af01d4dec3ae7fbbdf84f9f3c0a7

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

**container_name:** mailrise

**image:** yoryan/mailrise:1.4.0@sha256:66082168090b9a83f01cc71a9d7b1994840adbbbffbe4d2cf644272fbbc23a1a

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:29.0.3-apache@sha256:3ad47054206bdf4ad03cc33bd2a3691d9df277e21d1b081cd7c8bdb60dc5219f

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:29.0.3-apache@sha256:3ad47054206bdf4ad03cc33bd2a3691d9df277e21d1b081cd7c8bdb60dc5219f

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.4.2@sha256:e59ba8783bf7bc02a4779f103bb0d8751ac0e10f9471089709608377eded7aa8

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

### Service: nextcloud-redis

**container_name:** nextcloud-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

## docker/ansible/templates/compose-modules/nodeexporter.yml

### Service: nodeexporter

**container_name:** nodeexporter

**image:** prom/node-exporter:v1.8.2@sha256:4032c6d5bfd752342c3e631c2f1de93ba6b86c41db6b167b9a35372c139e7706

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

**image:** docker.io/library/postgres:16.3-alpine@sha256:de3d7b6e4b5b3fe899e997579d6dfe95a99539d154abe03f0b6839133ed05065

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.8.0@sha256:aa3e3448565e163ead65ce5eca6f46beb555121ad1079e55ad242165e801c73b

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:20db3df89eaeb1b271dd840888fe909b88b12f4b86ef641ec07a1d45d4c5168f

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.11.0@sha256:da0476cea301df8bc8d20739f0e76de1e77d91ad2c9170b45c803468dde19208

**url:** paperless.$DOMAINNAME

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

**url:** papermerge.$DOMAINNAME

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

**container_name:** photoprism

**image:** photoprism/photoprism:preview@sha256:af1b25641d169c0bde7406ff8ca088a297d9a5e67672b63f6668c5742159d6e8

**url:** photos.$DOMAINNAME

### Service: photoprism-db

**container_name:** photoprism-db

**image:** mariadb:11.4.2@sha256:e59ba8783bf7bc02a4779f103bb0d8751ac0e10f9471089709608377eded7aa8

### Service: photoprism-db-backup

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:5b8054e629cd39f6b2abeb6a88f257b817de4e4d5e4d8be3ce1bc0e33e109899

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.40.4.8679-424562606@sha256:e06a8af0b30250f4efd8392b55a3d56578919f94fa2ac9eaee14998f9d22af56

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.20.3-alpine@sha256:a6f635877e0daa4aa39c1cbf4e73a31b35d342284588fa72fd8a91efb3c6a091

**url:** portainer-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:f66d1d802ad387f523ec89b7ae872c12396e4b996c0e21a1930e6a1d0b9205b4

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

**container_name:** prometheus

**image:** prom/prometheus:v2.53.1@sha256:f20d3127bf2876f4a1df76246fca576b41ddf1125ed1c546fbd8b16ea55117e6

**url:** prometheus.$DOMAINNAME

### Service: pushgateway

**container_name:** pushgateway

**image:** prom/pushgateway:v1.9.0@sha256:98a458415f8f5afcfd45622d289a0aa67063563bec0f90d598ebc76783571936

**url:** pushgateway.$DOMAINNAME

## docker/ansible/templates/compose-modules/promtail.yml

### Service: promtail

**container_name:** promtail

**image:** grafana/promtail:3.1.0@sha256:b3db8e7b1cba0e8c45ce2ae72ebddfd88ebdcae86383f1680edf0074e9010ff6

**url:** promtail.$DOMAINNAME

### Service: promtail-docker-proxy

**container_name:** promtail-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.1-r0@sha256:f66d1d802ad387f523ec89b7ae872c12396e4b996c0e21a1930e6a1d0b9205b4

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

**image:** lscr.io/linuxserver/unifi-network-application:version-8.2.93@sha256:a78ea6ffe3d8d2a4f1a6b7233848c5bf563a345d0cdb10f88e4536ca79e028da

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.12@sha256:54996a559c724c726a31fb8131e1c9088a05f7e531760e2897212389bbf20fed

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

## docker/ansible/templates/compose-modules/uptime-kuma.yml

### Service: uptime-kuma

> :warning: **Deprecation Notice:** Replaced by: Gatus

**container_name:** uptime-kuma

**image:** louislam/uptime-kuma

## docker/ansible/templates/compose-modules/vault.yml

### Service: vault

**container_name:** vault

**image:** hashicorp/vault:1.17@sha256:0ba7c9c2922b5645c07fb363a7862fd79eee235004b8bcf7ecba26ccfbc48526

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

**image:** mariadb:11.4.2@sha256:e59ba8783bf7bc02a4779f103bb0d8751ac0e10f9471089709608377eded7aa8

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.1.3@sha256:79697ba2f5ab61e644e8a20e860003af2c12ed40335d80eca33d831c1b829ea4

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
