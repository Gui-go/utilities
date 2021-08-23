

pwd

# ls - list directory contents
ls
ls -la 
ls -lt  # list base on time and date
ls -ltr # list base on time and date revertedma
ls -FR . # To see recursively all dirs and files
ls *.txt # list all files that ends with .txt



#
cd 
cd /var/log/

# su - run a command with substitute user and group ID
su
su - # back to root

# cp - copy files and directories
cp 



rm

rmdir

locate

# stat - display file or file system status
stat Documents/ # Gets indo about the dir
stat -c '%A %a %n' * # Gets detailed permission info about file in current dir
stat --version


#
grep -r SOMETXT . # Search for sometxt in every file and returns where they were found