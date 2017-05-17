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
#change working directory
curDir=`pwd`
cd $PROJECT_HOME

#activate a virtualenv
. venv/bin/activate

#install pip packages
#ipython provides a nice repl, not needed for selenium
pip install selenium ; pip install ipython

#return where we were
cd \$curDir
"

  echo -e "
${HL}#Please continue running below script manually${EC}
"
#endregion print next manual steps
