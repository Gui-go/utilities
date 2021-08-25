#!/bin/bash

# Finds out whether a number is even or odd

read -p "Enter a number: " number

if [ `expr $number % 2` -eq 0 ]; then
    echo "${number} is even"
else
    echo "${number} is odd"
fi