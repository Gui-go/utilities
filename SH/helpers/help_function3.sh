#!/bin/bash

arg=$(seq $1)
# echo $arg

mkdir_recursively () {
    echo "dir_$1"
    # mkdir "dir_$i"
}

for i in $arg
do
    mkdir_recursively $i 
done 
