#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#Start a normal Chrome binary with the --headless command line flag (Linux-only for now)
google-chrome --headless --disable-gpu --remote-debugging-port=9222 https://chromium.org

#Navigate to http://localhost:9222 in another browser to open the DevTools interface or use a tool such as Selenium to drive the headless browser
#ref. https://chromium.googlesource.com/chromium/src/+/lkgr/headless/README.md
