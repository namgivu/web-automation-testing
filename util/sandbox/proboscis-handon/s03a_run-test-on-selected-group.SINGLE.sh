#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util

echo -e "\n${HL}Run group 'number'${EC}"
python "$SCRIPT_HOME/run_test.py" --group=number

echo -e "\n${HL}Run group 'string'${EC}"
python "$SCRIPT_HOME/run_test.py" --group=string
