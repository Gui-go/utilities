


# To create ssh key in the rsa format
# -C "<comment>"
ssh-keygen -t rsa -C guilhermeviegas1993@gmail.com

# Enter file name and passwd
# Get the key fingerprint
SHA256:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ls ~/.ssh
cat ~/.ssh/id_rsa.pub

# Post the ssh-rsa key and email to the security breach (such as github)

ssh -T git@github.com
# Insert the passwd


# -------------------------------------

ssh username@hostname

scp index.html username@hostname 

ssh-copy-id username@hostname 

# --------------------------------------------

# Generate a pair of public and private ssh keys
# --type rsa
# --bits 4096
ssh-keygen -t rsa -b 4096 

cd ~/.ssh 



scp index.html username@hostname:src/index.html