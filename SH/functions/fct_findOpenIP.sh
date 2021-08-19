#!/bin/bash

if [ "$1" == ""]
then
echo "Syntax: ./findUsedPorts.sh <ip>"
echo "You need to provide an ip address"

else 
rm $2 && touch $2
for ip in `seq 1 254`; do
echo Checking ip $1.$ip ----------------------------------------------------------------------- &
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d "():" >> $2 &
done

fi 
