#!/bin/bash

echo ""

echo "\$0 returns the name of the file: $0"

seq -s= 13 | tr -d '[:digit:]'

echo $0

printf %13s | tr " " "="

echo "\n"

