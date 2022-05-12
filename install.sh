#!/bin/bash
apt install python3 python3-pip git -y
pip install flask waitress
git clone https://github.com/nasrulnoor/doorbell_flask.git
cd doorbell_flask
cp -r webapp /usr/bin/webapp
cp doorbell.service /lib/systemd/system
systemctl enable doorbell
systemctl start doorbell
