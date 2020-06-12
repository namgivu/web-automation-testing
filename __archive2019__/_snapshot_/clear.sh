#!/usr/bin/env bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)  # get SH aka SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path

rm -rf  ${SH}/vault/20*
