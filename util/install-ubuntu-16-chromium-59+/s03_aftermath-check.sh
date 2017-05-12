#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#after installed Chrome 59+, verify the version
echo -e "
${CM}Chrome stable${EC}
`$chrome_stable --version`

${CM}Chrome 59+ aka. Chrome beta${EC}
`$chrome_beta   --version`
`$chrome59      --version`
`$chrome        --version`

${CM}Assumption${EC}
From now on
to run Chromium 59+ we use ${HL}\$chrome${EC} or \$chrome59 or \$chrome_beta
to run normal/stable Chrome we use \$chrome_stable
"
