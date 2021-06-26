


# To create ssh key in the rsa format
ssh-keygen -t rsa -C guilhermeviegas1993@gmail.com

# Enter file name and passwd
# Get the key fingerprint
SHA256:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ls ~/.ssh
cat ~/.ssh/id_rsa.pub

# Post the ssh-rsa key and email to the security breach (such as github)

ssh -T git@github.com
# Insert the passwd