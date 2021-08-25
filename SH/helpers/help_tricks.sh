





# Returns the 10 most commom commands in history
history | cut -c8- | sort | uniq -c | sort -rn | head

# Interactive remmemberer of code (reverse-i-search)
ctrl + r 

# Go to the beginning of the command/line
ctrl + a 

# Go to the end of the command/line
ctrl + e 

# Empty a file
> filename

# sudo apt install cowsay
echo "Hi, Humans" | cowsays

# nohup  -  run  a  command immune to hangups, with output to a non-tty
# nohup command let ur programm run in the background

# Login as root
sudo su        # not a best practice

# shred - overwrite a file to hide its contents, and optionally delete it
# completely deletes a file
# To completely delete the file and fill the space it was using with zeros, use the shred command. Use it like this: shred -zvu <filename>

# -x  => Use encryption when writing vim files.
vim -x filename

# w - Show who is logged on and what they are doing.
w 

# Get main information about the system
# sudo apt install screenfetch
screenfetch

# apropos - pesquisa por nomes e descrições de páginas de manual
# Faz sugestões de comandos
apropos math 
apropos docker

# Shutdown at a specific time
sudo shutdown 21:00

# lslogins - display information about known users in the system
# -u, --user-accs   =>   Show  user accounts.
# use sudo for a complete view
sudo lslogins
sudo lslogins -uf # list of failed login
sudo lslogins | awk '$3 >= 10 {print}' # List accounts running more than 10 processes








