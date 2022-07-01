#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo "You need a challenge name and port for the web server"
    echo "Ex. ./setup.sh xss 8080"
    exit 1
fi

sudo apt-get install pip flask-mysqldb mysql mysql-server

sudo pip install flask-sqlalchemy flask-session passlib

sed -i "s/##CHALLENGE_NAME##/$1/g" vuln/config.py
sed -i "s/##CHALLENGE_NAME##/$1/g" default.sql
sed -i "s/##CHALLENGE_PORT##/$2/g" vuln/config.py

