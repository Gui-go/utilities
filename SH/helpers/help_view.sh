


# echo - display a line of text
echo Hello world
echo "Hello world"
echo "My name is $(whoami)"
echo "My name is $(whoami)" | tr " "  "\n"


nano
vi
vim
gedit

# tail - output the last part of files
tail /var/log/syslog 
tail /var/log/auth.log
tail -f /var/log/syslog # Lets open stdout windown to check incoming updates 
# afonso
# cat - concatenate files and print on the standard output
cat 
cat /etc/passwd
sudo cat /etc/shadow
cat /var/log/auth.log | grep guilherme
cat /var/log/syslog | grep guilherme

# grep, egrep, fgrep, rgrep - print lines that match patterns
grep 


cut

# tr - translate or delete characters
# tr é bom pra fazer sumir caracteres indesejados no stdout
tr 
cat domains.txt | tr [:lower:] [:upper:]
cat linux.txt | tr [a-z] [A-Z]
ping www.google.com -c 1 | grep "64 bytes" | cut -d " " -f 5 | tr -d "():" # -f 5 (para versão em pt)
echo "My name is $(whoami)" | tr " "  "\n" # switches " " to to "\n"

# sort - sort lines of text files
sort file.txt # sort by line (works for simple text files)
netstat -ano | sort -k 5 # check all used port ordered by port (column 5)

history

# du - disk usage - estimate file space usage
du /var/log/                       # checks the size of each file in the directory
du -h /home/guilherme/Documentos/  # checks the size of each file in the directory in human format
du -h -d1 /home/guilherme/Documentos/proj_dir/ # checks the size of each file in the directory in human format in d depth

# find - search for files in a directory hierarchy
find . -name teste.txt  # Search for teste.txt file in the current directory
find . -iname teste.txt # Search for teste.txt file in the current directory ignoring case
find / -type d -name proj_dir # Search for directories called proj_dir everywhere
find /home/guilherme -type d -name proj_dir # Search for proj_dir dir at /home/guilherme directory
find . -type f -name teste.txt # -type f for files
find . -type f -name "*.php"
find . -type f -name "teste.txt" -exec rm -f {} \;  # Find and remove teste.txt file
find . -type f -name ".*" # Find all hidden files in /tmp dir
find . -user guilherme -name teste.txt # Find files called teste.txt owned by guilherme
find /home/guilherme/Documentos/proj_dir -user guilherme # Find every document owned by guilherme at /home/guilherme/Documentos/proj_dir
find /home -group developers
find /home -user guilherme -iname "*.txt"
find ./Documentos/proj_dir/ -cmin -60 # Find every file at the ./Documentos/proj_dir/ dir that was changed in the last 60 minutes
find ./Documentos/proj_dir/ -mmin -60  # Find every file at the ./Documentos/proj_dir/ dir that was modified in the last 60 minutes
find ./Documentos/proj_dir/ -amin -60
find . -size +50M -size -100M # Find all the files between 50M and 100M size
find / -type f -size +100M -exec rm -f {} \; # Find all files in the root dir greater than 100M and rm it
find / -type f -name *.mp3 -size +10M -exec rm {} \;