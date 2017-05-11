#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region build chromium

  #note current dir
  curDir=`pwd`

  #do build chromium
  cd $CHROMIUM_SRC
  ninja -C out/Default chrome

  #back to where we were
  cd $curDir

##endregion build chromium

