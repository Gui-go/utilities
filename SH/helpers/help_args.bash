#!/bin/bash


echo "$# arguments were passed"

echo "First argument is: $1"

echo "Second argument is: $2"

echo "Third argument is: $3"

echo "Forth argument is: $4"

echo "This file is called: $0"

echo "Here are them all: $@"

arg_array=("$@")                        # leave no spaces 
echo "arg_array[0]: ${arg_array[0]}"
echo "arg_array[1]: ${arg_array[1]}"
echo "arg_array[2]: ${arg_array[2]}"

# bash help_args.bash arg1 arg2 arg3 arg4 arg5