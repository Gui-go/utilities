#! /bin/bash

echo "Enter file to remove:"
read fileName

if [[ -f "$fileName" ]]
then
    rm $fileName
    echo "$fileName removed"
else
    echo "$fileName doesn't exists"
fi
