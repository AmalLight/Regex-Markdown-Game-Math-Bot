#!/bin/bash

ip=***
pass=***

sshpass -p $pass ssh -t $ip "pkill pybot; pkill firefox"
sshpass -p $pass scp *.py $ip:
sshpass -p $pass ssh -t $ip "chmod 744 *.py"

installa=" echo $pass | sudo -S ln -s /bin/python3 /bin/py; "
installa+="echo $pass | sudo -S apt-get install -y python3-pip xclip xsel; "

pipinstl="py -m pip"

installa+="echo $pass | sudo -S $pipinstl install -U pip; "
installa+="echo $pass | sudo -S $pipinstl install pynput pyperclip clipboard;"

sshpass -p $pass ssh -t $ip "$installa"
