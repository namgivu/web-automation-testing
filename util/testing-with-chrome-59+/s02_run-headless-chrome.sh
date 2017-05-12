#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#print guide
echo -e "
#Navigate to ${CM}http://localhost:9222${EC} in another browser to open the DevTools interface or use a tool such as Selenium to ${CM}drive the headless browser${EC}
#ref. https://chromium.googlesource.com/chromium/src/+/lkgr/headless/README.md
"

#Start a normal Chrome binary with the --headless command line flag (Linux-only for now)
chrome \
  --headless \                   #Runs Chrome in headless mode
  --disable-gpu \                #Temporarily needed for now
  --remote-debugging-port=9222 \
  https://www.chromestatus.com   #URL to open. Defaults to about:blank
