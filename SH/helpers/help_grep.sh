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