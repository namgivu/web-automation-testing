#!/usr/bin/env bash

##region common bash util
  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region Get the code

  #Create a chromium directory for the checkout and change to it - the full path has no spaces
  rm -rf $CHROMIUM_HOME ; mkdir -p $CHROMIUM_HOME
  cd $CHROMIUM_HOME

  #Run the fetch tool from depot_tools to check out the code and its dependencies.
  #If you don't want the full repo history, you can save a lot of time by adding the --no-history flag to fetch.
  fetch --no-history --nohooks chromium #run for at least 30 minutes

##endregion Get the code
