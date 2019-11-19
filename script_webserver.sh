#!/bin/bash
export PATH=/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
sudo apt-get update
sudo apt install python3-pip -y
pip3 install flask flask_restful
python3 Cloud-APSs/aps1.py
