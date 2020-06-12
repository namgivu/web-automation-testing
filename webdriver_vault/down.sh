#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"
    docker ps -qa     -f name=${STACK_NAME}_
    # list container  filtered by this prefix in container name eg wdv_
