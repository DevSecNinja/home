# Docker Information

## docker/ansible/templates/compose-modules/adguard.yml

### Service: adguard

**container_name:** adguard

**image:** adguard/adguardhome:v0.107.53@sha256:d9c512051141e6a617d773f16cdf6782c178464c6e766acf9fe63482a171f95c

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

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/bitwarden.yml

### Service: bitwarden

**container_name:** bitwarden

**image:** bitwarden/self-host:2024.9.2-beta@sha256:8d90075358899c5d35e6210ef41a18428533f81d44edb17e860b04d4294f3d37

**url:** bitwarden.$DOMAINNAME

### Service: bitwarden-db

**container_name:** bitwarden-db

**image:** mariadb:11.5.2@sha256:9e7695800ab8fa72d75053fe536b090d0c9373465b32a073c73bc7940a2e8dbe

### Service: bitwarden-db-backup

**container_name:** bitwarden-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/cadvisor.yml

### Service: cadvisor

**container_name:** cadvisor

**image:** gcr.io/cadvisor/cadvisor:v0.50.0@sha256:2f3ea45c7ee3d7a0ce9f9d55a5053bd12285b02aca307ce9657af8e3ea7f6761

**url:** cadvisor-noauth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/change-detection.yml

### Service: change-detection

**container_name:** change-detection

**image:** ghcr.io/dgtlmoon/changedetection.io:0.46.04@sha256:cfe4379f448e71ed7c0030b00562c678f5349d0b209b8d4985df20826af38e93

**url:** change-detection.$DOMAINNAME

## docker/ansible/templates/compose-modules/cloudflare-companion.yml

### Service: cloudflare-companion

**container_name:** cloudflare-companion

**image:** tiredofit/traefik-cloudflare-companion:7.3.2@sha256:716a265a69f5f75ddbb089c19fe8e4b52cfd891f1dd426fe0e525a3ddf941ac8

## docker/ansible/templates/compose-modules/cloudflare.yml

### Service: cloudflare-ddns

**container_name:** cloudflare-ddns

**image:** favonia/cloudflare-ddns:1.14.2@sha256:9e410575e7c093b8ff3236dba72f0af032f95f26c50a92fbcad8f29f0e19ff87

## docker/ansible/templates/compose-modules/code-server.yml

### Service: code-server

**container_name:** code-server

**image:** lscr.io/linuxserver/code-server:version-4.89.0@sha256:678e01467fecf0d1d32b938f3f5324a69f74f9187d37fadddb8f926024524b8b

**url:** code.$DOMAINNAME

## docker/ansible/templates/compose-modules/cyberchef.yml

### Service: cyberchef

**container_name:** cyberchef

**image:** ghcr.io/gchq/cyberchef:10.19.2@sha256:04a2be6fb9db9a65b6dc148f3c52be499f40ecb281b69135783bbd76186b1513

**url:** cyberchef.$DOMAINNAME

## docker/ansible/templates/compose-modules/dozzle.yml

### Service: dozzle

**container_name:** dozzle

**image:** amir20/dozzle:v8.5.5@sha256:aa9ea440a33c45fb25d59e06cb6850e6655404fad4bebac6345d8535b9d8a9ee

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

**image:** mendhak/http-https-echo:34@sha256:b9b45336763a8ee7f34b78fc77f3b1ecbaae41bb9ab72949d06e7c3cf6928532

**url:** echo-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/excalidraw.yml

### Service: excalidraw

**container_name:** excalidraw

**image:** excalidraw/excalidraw:latest@sha256:df3ddf00d7977d7007ea33b5397239ff20955eeeeafd38735cb1604be799564a

**url:** excalidraw.$DOMAINNAME

## docker/ansible/templates/compose-modules/folding-at-home.yml

### Service: foldingathome

**container_name:** foldingathome

**image:** lscr.io/linuxserver/foldingathome:version-8.3.18@sha256:97c7346a05a2993ff70defa3b33660c1d694b04e97691b2765838fd3e14361ae

## docker/ansible/templates/compose-modules/gatus.yml

### Service: gatus

**container_name:** gatus

**image:** twinproduction/gatus:v5.12.1@sha256:e808d45f327450a42d8f670160bf4a596950dfd2824aea3825f03b49c2d7e61c

**url:** status.$DOMAINNAME

### Service: gatus-db

**container_name:** gatus-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:d898b0b78a2627cb4ee63464a14efc9d296884f1b28c841b0ab7d7c42f1fffdf

### Service: gatus-db-backup

**container_name:** gatus-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/grafana.yml

### Service: grafana

**container_name:** grafana

**image:** grafana/grafana:11.2.2@sha256:d5133220d770aba5cb655147b619fa8770b90f41d8489a821d33b1cd34d16f89

**url:** grafana.$DOMAINNAME

### Service: loki

**container_name:** loki

**image:** grafana/loki:3.2.0@sha256:882e30c20683a48a8b7ca123e6c19988980b4bd13d2ff221dfcbef0fdc631694

**url:** loki.$DOMAINNAME

## docker/ansible/templates/compose-modules/home-assistant.yml

### Service: home-assistant

**container_name:** home-assistant

**image:** ghcr.io/home-assistant/home-assistant:beta@sha256:4576a54b0771dd1438a08d9af7fdc2ff7bc054abd5dc76d35236c963b9694f7c

**url:** home-assistant.$DOMAINNAME

## docker/ansible/templates/compose-modules/homepage.yml

### Service: homepage

**container_name:** homepage

**image:** ghcr.io/gethomepage/homepage:v0.9.10@sha256:671c2ed1a61b5dfbb9a1998c8738c3aeb1acf11adbc12563f81fcf4fd9802198

**url:** homepage-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: homepage-docker-proxy

**container_name:** homepage-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

## docker/ansible/templates/compose-modules/hoppscotch.yml

### Service: hoppscotch

**container_name:** hoppscotch

**image:** hoppscotch/hoppscotch:2024.9.0@sha256:ae01b6e3abe4d4529dd9e7cab604ebfea2f318202899c8611600f7388d753b39

**url:** api-tester.$DOMAINNAME

### Service: hoppscotch-db

**container_name:** hoppscotch-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:d898b0b78a2627cb4ee63464a14efc9d296884f1b28c841b0ab7d7c42f1fffdf

### Service: hoppscotch-db-backup

**container_name:** hoppscotch-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/influxdb.yml

### Service: influxdb

**container_name:** influxdb

**image:** influxdb:2.7-alpine@sha256:327be0243a329b1da350a37c1468d756f4258330d50d10a2a993e5bb9a6e3d2e

**url:** influxdb-noauth.$DOMAINNAME

### Service: influxdb-backup

**container_name:** influxdb-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

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

**image:** sissbruecker/linkding:1.35.0-alpine@sha256:5c830acf9ce284b7eb9ca51c50125de5e85dd0a35bba1920c83420550ee34c17

**url:** linkding.$DOMAINNAME

### Service: linkding-db

**container_name:** linkding-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:d898b0b78a2627cb4ee63464a14efc9d296884f1b28c841b0ab7d7c42f1fffdf

### Service: linkding-db-backup

**container_name:** linkding-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/lobe-chat.yml

### Service: lobe-chat

**container_name:** lobe-chat

**image:** lobehub/lobe-chat:v1.20.5@sha256:3fe2569ac14ae4fc03719121a53b9487df9484333fc9dca78a777e7b766e0771

**url:** chat.$DOMAINNAME

## docker/ansible/templates/compose-modules/mailrise.yml

### Service: mailrise

**container_name:** mailrise

**image:** yoryan/mailrise:1.4.0@sha256:66082168090b9a83f01cc71a9d7b1994840adbbbffbe4d2cf644272fbbc23a1a

## docker/ansible/templates/compose-modules/n8n.yml

### Service: n8n

**container_name:** n8n

**image:** n8nio/n8n:1.61.0@sha256:f3b32e42765bc0aebc747d06df0ea3b8a0931343b49108ab3bf1dfd579ee6e65

**url:** n8n.$DOMAINNAME

### Service: n8n-db

**container_name:** n8n-db

**image:** docker.io/library/postgres:16.4-alpine@sha256:d898b0b78a2627cb4ee63464a14efc9d296884f1b28c841b0ab7d7c42f1fffdf

### Service: n8n-db-backup

**container_name:** n8n-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/nextcloud.yml

### Service: nextcloud

**container_name:** nextcloud

**image:** nextcloud:30.0.0-apache@sha256:6b89c15912462b5849b2ee73c2effc73afdd2a826366222b7d021d94f9bb1df5

**url:** cloud.$DOMAINNAME

### Service: nextcloud-cron

**container_name:** nextcloud-cron

**image:** nextcloud:30.0.0-apache@sha256:6b89c15912462b5849b2ee73c2effc73afdd2a826366222b7d021d94f9bb1df5

### Service: nextcloud-db

**container_name:** nextcloud-db

**image:** mariadb:11.5.2@sha256:9e7695800ab8fa72d75053fe536b090d0c9373465b32a073c73bc7940a2e8dbe

### Service: nextcloud-db-backup

**container_name:** nextcloud-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

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

**image:** docker.io/library/postgres:16.4-alpine@sha256:d898b0b78a2627cb4ee63464a14efc9d296884f1b28c841b0ab7d7c42f1fffdf

### Service: paperless-db-backup

**container_name:** paperless-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

### Service: paperless-gotenberg

**container_name:** paperless-gotenberg

**image:** docker.io/gotenberg/gotenberg:8.11.0@sha256:e60da3ecc52050303c3886630aa7ed82f9486660b82a1ce6e5bf253c3b0764d4

### Service: paperless-redis

**container_name:** paperless-redis

**image:** redis:alpine3.19@sha256:892b41c092a599f76c30b48e9dcfb185ce8cea3560970b1c4f2745c89bb34344

### Service: paperless-tika

**container_name:** paperless-tika

**image:** ghcr.io/paperless-ngx/tika:2.9.1-minimal@sha256:20db3df89eaeb1b271dd840888fe909b88b12f4b86ef641ec07a1d45d4c5168f

### Service: paperless-web

**container_name:** paperless-web

**image:** ghcr.io/paperless-ngx/paperless-ngx:2.12.1@sha256:217cec76128c2545872cf356694f2ffd4524cb84892d0333e654795dec255633

**url:** paperless.$DOMAINNAME

## docker/ansible/templates/compose-modules/papermerge.yml

### Service: papermerge

**container_name:** papermerge

**image:** papermerge/papermerge:3.2.0@sha256:11bd6e47622b295ee40f1e719c63235544121839a30e5083d959208931007b62

**url:** papermerge.$DOMAINNAME

## docker/ansible/templates/compose-modules/photoprism.yml

### Service: photoprism

**container_name:** photoprism

**image:** photoprism/photoprism:preview@sha256:22f2258f64dbe3aca5bafee6eeaaf80c8b1cd6fe4e9d16561743d08e08cea6fa

**url:** photos.$DOMAINNAME

### Service: photoprism-db

**container_name:** photoprism-db

**image:** mariadb:11.5.2@sha256:9e7695800ab8fa72d75053fe536b090d0c9373465b32a073c73bc7940a2e8dbe

### Service: photoprism-db-backup

**container_name:** photoprism-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/phpmyadmin.yml

### Service: phpmyadmin

**container_name:** phpmyadmin

**image:** phpmyadmin:5.2.1-apache@sha256:0e1c550eda821813ab958a50dd0d44d17e129c87beb1d4c5f14ca34b3949e92d

**url:** phpmyadmin.$DOMAINNAME

## docker/ansible/templates/compose-modules/plex.yml

### Service: plex

**container_name:** plex

**image:** lscr.io/linuxserver/plex:version-1.41.0.8992-8463ad060@sha256:6facc481ef321946066db33d90c4e950c9910e5ec14d61b3f5b467745bf2cc81

**url:** plex-noauth.$DOMAINNAME

## docker/ansible/templates/compose-modules/portainer.yml

### Service: portainer

**container_name:** portainer

**image:** portainer/portainer-ce:2.21.2-alpine@sha256:7f93a7f68e95e2a6c989487e213817f2e9fa1010a7aaf6ac6304397b40e81b92

**url:** portainer-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

### Service: portainer-docker-proxy

**container_name:** portainer-docker-proxy

**image:** lscr.io/linuxserver/socket-proxy:version-1.26.2-r0@sha256:792bdde50356861db095884bb914f2e7004a851d92301a0c7150ea174be26864

## docker/ansible/templates/compose-modules/prometheus.yml

### Service: prometheus

**container_name:** prometheus

**image:** prom/prometheus:v2.54.1@sha256:f6639335d34a77d9d9db382b92eeb7fc00934be8eae81dbc03b31cfe90411a94

**url:** prometheus.$DOMAINNAME

### Service: pushgateway

**container_name:** pushgateway

**image:** prom/pushgateway:v1.10.0@sha256:7a4d0696a24ef4e8bad62bee5656855a0aff2f26416d8cb32009dc28d6263604

**url:** pushgateway.$DOMAINNAME

## docker/ansible/templates/compose-modules/promtail.yml

### Service: promtail

**container_name:** promtail

**image:** grafana/promtail:3.2.0@sha256:a77ce6cc7d6f1a05611adeaef863935f66d68640d9d0ef2feb190c8f0edac19e

**url:** promtail.$DOMAINNAME

### Service: promtail-docker-proxy

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

**image:** ghcr.io/jordemort/traefik-forward-auth:latest@sha256:394f86bff5cc839fac1392f65dd3d4471e827bc29321a4460e7d92042e026599

**url:** auth-$GENERIC_HOSTNAME_SUFFIX.$DOMAINNAME

## docker/ansible/templates/compose-modules/unifi.yml

### Service: unifi

**container_name:** unifi

**image:** lscr.io/linuxserver/unifi-network-application:version-8.4.62@sha256:b97f24e2ebfb8b096dadde3a77f2354c037244f24adb1517240173ede0eb28b8

**url:** unifi.$DOMAINNAME

### Service: unifi-db

**container_name:** unifi-db

**image:** mongo:7.0.14@sha256:244afb1488edfc42aaa8ffa6153393bbc075d63516ab0305daa2eaa35241eb52

### Service: unifi-db-backup

**container_name:** unifi-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

## docker/ansible/templates/compose-modules/uptime-kuma.yml

### Service: uptime-kuma

> :warning: **Deprecation Notice:** Replaced by: Gatus

**container_name:** uptime-kuma

**image:** louislam/uptime-kuma

## docker/ansible/templates/compose-modules/vault.yml

### Service: vault

**container_name:** vault

**image:** hashicorp/vault:1.17@sha256:dabbf3fd2ef0858795848a61c6b6865305eec16b144e03dfc6a550a13b0211e6

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

**image:** mariadb:11.5.2@sha256:9e7695800ab8fa72d75053fe536b090d0c9373465b32a073c73bc7940a2e8dbe

### Service: wallabag-db-backup

**container_name:** wallabag-db-backup

**image:** tiredofit/db-backup:4.1.4@sha256:6df3a87b288d00d2f00f87f3dd2314eba793d3a34b500d3fcef3a1b598946e3d

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

**image:** benbusby/whoogle-search:latest@sha256:9f9cd9229b32487c77aa9bd50bf2c54ca5053e78d2881e6cbee70dac7cb0dd64

**url:** search.$DOMAINNAME

## docker/ansible/templates/compose-modules/wireguard.yml

### Service: wireguard

**container_name:** wireguard

**image:** lscr.io/linuxserver/wireguard:version-v1.0.20210914@sha256:c3c7a910e46c9bd25daf22e38bb48cbc10d32727c5ee1fe5ede32ee4c34f6a36

**url:** wireguard.$DOMAINNAME
