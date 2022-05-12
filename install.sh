#!/bin/bash
apt install python3 python3-pip -y
pip install flask waitress
git clone https://github.com/assynergy/flask_app.git
cd flask_app
cp webapp /usr/bin/webapp
cp doorbell.service /lib/systemd/system
systemctl enable doorbell
systemctl start doorbell
