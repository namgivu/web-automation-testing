#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util


#download
PLATFORM=linux64 #platform options: linux32, linux64, mac64, win32
VERSION=$(curl -s http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
DOWNLOAD_URL="http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
TMP_ZIP='/tmp/chromedriver.zip'
curl $DOWNLOAD_URL > $TMP_ZIP

#unpack
sudo apt-get install -y bsdtar
bsdtar -xvf $TMP_ZIP -C "$PROJECT_HOME/venv/bin/" #unzip using bsdtar ref. https://askubuntu.com/a/855993/22308

#aftermath
echo
which chromedriver
chromedriver --version