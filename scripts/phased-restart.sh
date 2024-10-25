#!/bin/bash

# Get the Unifi image version from the running container
RUNNING_VERSION=$(docker inspect --format '{{.Config.Image}}' unifi 2>/dev/null | grep -oP '(?<=lscr.io/linuxserver/unifi-network-application:)[^@]*')

# If the container doesn't exist or the image version can't be found
if [ -z "$RUNNING_VERSION" ]; then
    echo "Unifi container is not running or image version can't be found. Exiting..."
    exit 1
fi

# Get the new Unifi image version from the docker-compose file
NEW_VERSION=$(grep -oP '(?<=lscr.io/linuxserver/unifi-network-application:)[^@]*' docker-compose.yml)

# If the versions don't match
if [ "$NEW_VERSION" != "$RUNNING_VERSION" ]; then
    # Stop the database container
    docker compose stop unifi
    docker compose stop unifi-db

    docker compose up -d unifi unifi-db
else
    echo "Running version is the same as version in Docker compose: ${RUNNING_VERSION}"
    exit 0
fi
