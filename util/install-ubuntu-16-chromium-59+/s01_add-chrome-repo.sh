#!/usr/bin/env bash

#ref. https://www.tecmint.com/install-google-chrome-in-debian-ubuntu-linux-mint

#Download the key and then use apt-key to add it to the system
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

#After adding the key, run the following command to add chrome repository to your system sources
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

#After adding chrome repository, you must do a system update to update the newly added chrome repository
sudo apt-get update
