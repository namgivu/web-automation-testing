#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util

sudo pip install proboscis
sudo pip install yanc #report with color ref. https://stackoverflow.com/a/33506794/248616, official pip page ref. https://pypi.python.org/pypi/yanc