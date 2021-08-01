#! /bin/bash

echo "Enter filename to search text from:"
read fileName

if [[ -f $fileName ]]
then
    echo "Enter the text to search:"
    read grepVar

    echo "---------------------------"
    echo "Remember:
        -i, --ignore-case
        -n, --line-number
        -c, --count"

    echo "---------------------------"
    echo "grep $grepVar $fileName"
    var1=$(grep -c $grepVar $fileName)
    echo "Found: $var1"
    grep $grepVar $fileName
    
    echo "---------------------------"
    echo "grep -i -n $grepVar $fileName"
    var2=$(grep -i -n -c $grepVar $fileName)
    echo "Found: $var2"
    grep -i -n $grepVar $fileName

else
    echo "$fileName doenst exists"
fi