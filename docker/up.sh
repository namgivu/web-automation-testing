#!/usr/bin/env bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)  # get SH aka SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path

docker-compose  -f "$SH/docker-compose.yml"  -p 'myseleniumhub'  up  -d           --force-recreate --remove-orphans  # --scale selenium-node-ch=1  --scale selenium-node-ff=0
#               docker compose file          stack prefix            detach mode  do we need these?                  # scale multiple nodes if needed
#                                                                                 TODO
