#!/bin/bash

# There is some sort of bug in bash arrays
# https://stackoverflow.com/questions/25222259/i-am-getting-error-array-sh-3-array-sh-syntax-error-unexpected

#Simple array
array=(1 2 3 4 5)

echo ${array[*]}
echo ${array[@]}
echo "Run only $0"
echo "No need to use sh command"