#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"
    docker-compose  -f "$SH/docker-compose.yaml"  -p $STACK_NAME             up  -d
    #               docker-compose file path      prefix for container name  .   run as daemon
