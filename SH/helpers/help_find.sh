

# https://www.tecmint.com/35-practical-examples-of-linux-find-command/

# Find for tecmint.txt in the /home directory
find /home -iname tecmint.txt

# Find repo named diretories
find . -type d -name "*_repo"

# Find all PHP Files in Directory
find . -type f -name "*.php"

# Lists all diretories
find . -type d

# Lists all files
find . -type f

# Ranks all the txt files by number of lines
wc -l $(find . -name "*.txt") | sort -nr

find . -type d -iname "dir*" | xargs rm -rf # Find and remove every dir* directory in at current folder
time find . -type d -iname "dir*" | xargs rm -rf # To check time performance (xargs is much better than exec)

