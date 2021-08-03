#! /bin/bash

echo "Enter file name:"
read fileName

if [[ -f "$fileName" ]]
then
    echo "$fileName already exists"
else
    touch $fileName
    echo "File $fileName created"
fi