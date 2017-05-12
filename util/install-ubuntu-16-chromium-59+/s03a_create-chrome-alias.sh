#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#create chromium 59+ alias as 'chrome'
echo "
#region chrome alias
alias        chrome='google-chrome-beta'
alias      chrome59='google-chrome-beta'
alias   chrome_beta='google-chrome-beta'
alias chrome_stable='google-chrome-stable'

shopt -s expand_aliases #make bash script recognize ref. https://unix.stackexchange.com/a/1498/17671

echo -e '${CM}Alias for chromium 59+ created${EC}'
type chrome #aftermath check
#endregion chrome alias
" >> $BASHRC

echo -e "Please refresh your bash shell
source $BASHRC
"
