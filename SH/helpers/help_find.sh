

# https://www.tecmint.com/35-practical-examples-of-linux-find-command/


find /home -iname tecmint.txt # Find for tecmint.txt in the /home directory
find . -type d -name "*_repo" # Find repo named diretories
find . -type f -name "*.php" # Find all PHP Files in Directory
find . -type d # Lists all diretories
find . -type f # Lists all files
wc -l $(find . -name "*.txt") | sort -nr # Ranks all the txt files by number of lines
find . -type d -iname "dir*" | xargs rm -rf # Find and remove every dir* directory in at current folder
time find . -type d -iname "dir*" | xargs rm -rf # To check time performance (xargs is much better than exec)
find . -type f -size 10M # Find files that are bigger than 10M




