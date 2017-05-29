#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #import common setting
  source "$SCRIPT_HOME/s00_config.sh"

##endregion common bash util

#unzip tool
sudo echo 'sudo initiated'
sudo apt-get install -y bsdtar
echo


#region download & unpack
  #do download
  PLATFORM=linux64 #platform options: linux32, linux64, mac64, win32
  VERSION=$(curl -s http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
  DOWNLOAD_URL="http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
  TMP_ZIP='/tmp/chromedriver.zip'
  curl $DOWNLOAD_URL > $TMP_ZIP

  #unpack using bsdtar ref. https://askubuntu.com/a/855993/22308
  sudo apt-get install -y bsdtar
  CHROMEDIRVER_HOME="$PROJECT_HOME/venv/bin/"
  bsdtar -xvf $TMP_ZIP -C "$CHROMEDIRVER_HOME" #unzip using bsdtar ref. https://askubuntu.com/a/855993/22308

  #make chromedriver command globally available
  sudo ln -s "$CHROMEDIRVER_HOME/chromedriver" /usr/local/bin/chromedriver
  sudo ln -s "$CHROMEDIRVER_HOME/chromedriver" /usr/bin/chromedriver

#endregion download & unpack


#aftermath
echo -e "
${CM}#Aftermath check${EC}
  version `chromedriver --version`
  path    `which chromedriver`
"



echo -e "
${CM}#Please run below script manually${EC}
  chromedriver
  #we must have it run successfully; the console to prompt 'Only local connections are allowed.'
"
