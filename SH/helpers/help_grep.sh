#!/bin/bash



-i, --ignore-case
-n, --line-number
-E, --extended-regexp

grep -in -E "senha|segredo|credential" $(find . -type f)
grep -in -E "senha|segredo|credential" $(find / -type f)
grep -in -E "senha|segredo|credential" $(find /etc -type f)
grep -in -E "senha|segredo|credential" $(find ./Documents/projects_dir/ -type f)

# Search for the word "let" (ignore case) in all files .txt from previous dir
grep -i "let" $(find .. -name "*.txt")

# Find out which shell the $USER is currently using (It might be dash, bash, or other)
grep $USER /etc/passwd

# Find out which shells are currently installed
cat /etc/shells

# Check whether a term is contained in a dir
grep -Pri Search_Term path_to_directory