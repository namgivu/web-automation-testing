#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util

#unzip tool
sudo apt-get install -y bsdtar
echo

#download & unpack
PLATFORM=linux64 #platform options: linux32, linux64, mac64, win32
VERSION=$(curl -s http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
DOWNLOAD_URL="http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
curl $DOWNLOAD_URL | bsdtar -xvf -C "$PROJECT_HOME/venv/bin/" #unzip using bsdtar ref. https://askubuntu.com/a/855993/22308

#aftermath
echo
which chromedriver
chromedriver --version

echo -e "
${CM}#Please run below script manually${EC}
#We must have it run successfully; the console to prompt 'Only local connections are allowed.'
chromedriver
"
