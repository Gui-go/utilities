#!/bin/bash

echo "Enter the file you want to sed (substitute value):"
read arg1

echo "Enter the value to substitute:"
read arg2 

echo "Enter substitution:"
read arg3

arg4="s/${arg2}/${arg3}/g"

if [[ -f $arg1 ]]
then 
    # sed -i 's/Linux/unix' $fileName # only the first one
    echo "Before:---------------------------"
    cat $arg1
    sed -i $arg4 $arg1
    echo ""
    echo "After:----------------------------"
    cat $arg1
    echo ""
else 
    echo "File $arg1 doesnt exists"
fi