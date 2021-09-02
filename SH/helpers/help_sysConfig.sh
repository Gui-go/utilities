


# passwd - change user password
passwd

# useradd - create a new user or update default new user information
useradd newuser
passwd newuser # Once the user is created, set the user password by running the passwd command
userdel newuser
userdel -r newuser # Use the -r (–remove) option to remove the user’s home directory and mail spool
groupadd mygroup
groupdel mygroup



# adduser,  addgroup  -  adiciona  um  utilizador  ou  grupo ao sistema
adduser
adduser <USER>


# usermod - modify a user account
usermod -aG sudo guigo # to give root privilege


# lsb_release - print distribution-specific information
# The lsb_release command provides certain LSB (Linux Standard Base) and distribution-specific information.
lsb_release -a


# chmod - change file mode bits
# r (read) = 4
# w (write) = 2
# x (execute) = 1
# no permissions = 0
chmod 644 filename
chmod 774 SH/helpers/help_function0.sh
chmod -R 755 dirname # For every file in the dir
find SH/helpers/help_function0.sh -printf "%m:%p\n"

# chown - change file owner and group
chown username filename
chown username:groupname filename
chown -R username:groupname dirname


# lsb_release - print distribution-specific information
# The lsb_release command provides certain LSB (Linux Standard Base) and distribution-specific information.
lsb_release -a


# Returns IP address (and others)
hostname -i
