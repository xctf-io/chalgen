#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo "You need a challenge name and challenge id"
    echo "Ex. ./setup.sh xss 2"
    exit 1
fi

sed -i "s/##CHALLENGE_NAME##/$1/g" default.sql
mysql -u root -ptoor < default.sql

i=$2
port=$[3306+$i]

mkdir /var/lib/mysql$i
chown -R mysql.mysql /var/lib/mysql$i/
mkdir /var/log/mysql$i
chown -R mysql.mysql /var/log/mysql$i
cp -R /etc/mysql/ /etc/mysql$i

cd /etc/mysql$i/
sed -i "s/3306/$port/g" my.cnf
sed -i "s/mysqld.sock/mysqld$i.sock/g" my.cnf
sed -i "s/mysqld.pid/mysqld$i.pid/g" my.cnf
sed -i "s/var\/lib\/mysql/var\/lib\/mysql$i/g" my.cnf
sed -i "s/var\/log\/mysql/var\/log\/mysql$i/g" my.cnf

mysql_install_db --user=mysql --datadir=/var/lib/mysql$i/

mysqld_safe --defaults-file=/etc/mysql$i/my.cnf &

