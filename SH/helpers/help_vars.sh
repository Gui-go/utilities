#! /bin/bash

nome="Guigo"
user=$(whoami)
nickname=$(whoami | cut -c 1-3)
dt=$(date '+%Y%m%d')

# echo - display a line of text
echo $nome
echo $user
echo $nickname
echo "A data de hoje é $dt"

# gpg - OpenPGP encryption and signing tool