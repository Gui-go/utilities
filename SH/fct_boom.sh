#! /bin/bash

echo "Press any key:"

while [ true ]
do
    read -t 3 -n 1 var
if [[ $var = 0 ]]
then
    echo "You have saved us all, thanks."
    exit;
else
    echo "Please, press a key"
fi

done 
