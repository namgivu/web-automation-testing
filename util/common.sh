#!/usr/bin/env bash

#coloring
HL='\033[1;33m' #high-lighted color
CM='\033[0;32m' #comment color
ER='\033[1;31m' #error color
EC='\033[0m'    #end coloring


#path
BASHRC="$HOME/.bashrc"


#region chrome alias
alias   chrome_beta='google-chrome-beta'
alias      chrome59='google-chrome-beta'
alias        chrome='google-chrome-beta' #chromium 59+ alias as 'chrome'
alias chrome_stable='google-chrome-stable'

shopt -s expand_aliases #make bash script recognize alias ref. https://unix.stackexchange.com/a/1498/17671

echo -e "${CM}Alias for chromium 59+ created${EC}"
type chrome #aftermath check by printing alias 'chrome'
echo
#endregion chrome alias
