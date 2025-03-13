#!/bin/sh

set -e

echo "My cmd: $DOCKER_CMD"

echo "Service started (env=$RUNNING_IN_ENV): $DOCKER_CMD"
    eval "$DOCKER_CMD"
    exit 0
