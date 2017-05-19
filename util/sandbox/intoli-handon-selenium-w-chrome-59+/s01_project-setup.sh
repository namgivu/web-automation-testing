#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#make the project directory
rm -rf $PROJECT_HOME && mkdir -p $PROJECT_HOME

#create a virtualenv
virtualenv $PROJECT_HOME/venv

#region print next manual steps
  echo -e "
${CM}#Please continue running below script manually${EC}

#activate a virtualenv
source $PROJECT_HOME/venv/bin/activate

#install pip packages
sudo -H pip install selenium
sudo -H pip install ipython #ipython provides a nice REPL shell environment, not needed for selenium
"

#endregion print next manual steps
