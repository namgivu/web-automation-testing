#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region aftermath check

  #note current dir
  curDir=`pwd`

  #run test
  cd $CHROMIUM_SRC
  out/Default/unit_tests --gtest_filter="PushClientTest.*"

  #run chromium
  #Once it is built, you can simply run the browser
  out/Default/chrome

  #back to where we were
  cd $curDir

##endregion aftermath check

