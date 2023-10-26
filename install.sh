#!/bin/bash
apt install python3 python3-pip git -y
pip3 install flask waitress telegram-send
git clone https://github.com/nashnoor/doorbell.git
cd doorbell_flask
#pip3 install -r requirements.txt
cp -r webapp /usr/bin/webapp
cp doorbell.service /lib/systemd/system
systemctl enable doorbell
systemctl start doorbell
