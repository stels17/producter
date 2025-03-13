#!/bin/sh

set -e

echo "My cmd: $DOCKER_CMD"

# You can put other setup logic here
#mkdir /var/logs
# Evaluating passed command:
#exec "$@"

echo "Service started (env=$RUNNING_IN_ENV): $DOCKER_CMD"
    eval "$DOCKER_CMD"
    exit 0
