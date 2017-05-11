#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


##region Install depot_tools

  #prepare folder
  rm -rf $DEPOT_TOOLS_HOME ; mkdir -p $DEPOT_TOOLS_HOME

  #Clone the depot_tools repository
  git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git $DEPOT_TOOLS_HOME

  #Add depot_tools to the end of your PATH (put this in your ~/.bashrc or ~/.zshrc)
  echo "
export PATH='\$PATH:$DEPOT_TOOLS_HOME'
" >> $BASHRC

##endregion Install depot_tools
