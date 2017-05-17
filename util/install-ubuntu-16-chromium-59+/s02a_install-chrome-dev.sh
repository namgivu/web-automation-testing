#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region download chrome 59+ from beta channel

  #ref. https://www.tecmint.com/install-google-chrome-in-debian-ubuntu-linux-mint

  #Install Chrome Beta Version
  sudo apt-get update
  sudo apt-get install -y google-chrome-unstable

##endregion download chrome 59+ from beta channel
