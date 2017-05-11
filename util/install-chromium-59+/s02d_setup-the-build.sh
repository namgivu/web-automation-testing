#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region setup the build

  #note current dir
  curDir=`pwd`

  #do setup the build
  cd $CHROMIUM_SRC
  gn gen out/Default

  #back to where we were
  cd $curDir

##endregion setup the build
