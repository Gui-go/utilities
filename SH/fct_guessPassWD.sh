#!/bin/bash

i=0
max=10
secret="passwd"
while [ $i -lt $max ]
do 
    echo "You have $(($max-$i)) attempts"
    read pass
    i=$(($i+1))
    if [ $pass = $secret ]
    then
        echo "Got it!"
        i=$(($max+1))
    elif [ $i = $max ]
    then
        echo "Booom!!"
    else
        echo "Try again"
    fi
done