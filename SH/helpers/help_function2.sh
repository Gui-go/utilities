#!/bin/bash

# Function 1
hello_parameter1() {
   echo "hello, $1"
}
hello_parameter1 "Guigo"

# Function 2 
arg1=$1
hello_parameter2() {
   echo "hello, $arg1"
}
hello_parameter2 "Guigo"



