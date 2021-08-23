#!/bin/bash

bold=`echo "\e[1m"`; underline=`echo "\e[4m"`; dim=`echo "\e[2m"`; strickthrough=`echo "\e[9m"`; blink=`echo "\e[5m"`; reverse=`echo "\e[7m"`; hidden=`echo "\e[8m"`; normal=`echo "\e[0m"`; black=`echo "\e[30m"`; red=`echo "\e[31m"`; green=`echo "\e[32m"`; orange=`echo "\e[33m"`; blue=`echo "\e[34m"`; purple=`echo "\e[35m"`; aqua=`echo "\e[36m"`; gray=`echo "\e[37m"`; darkgray=`echo "\e[90m"`; lightred=`echo "\e[91m"`; lightgreen=`echo "\e[92m"`; lightyellow=`echo "\e[93m"`; lightblue=`echo "\e[94m"`; lightpurple=`echo "\e[95m"`; lightaqua=`echo "\e[96m"`; white=`echo "\e[97m"`; default=`echo "\e[39m"`; BLACK=`echo "\e[40m"`; RED=`echo "\e[41m"`; GREEN=`echo "\e[42m"`; ORANGE=`echo "\e[43m"`; BLUE=`echo "\e[44m"`; PURPLE=`echo "\e[45m"`; AQUA=`echo "\e[46m"`; GRAY=`echo "\e[47m"`; DARKGRAY=`echo "\e[100m"`; LIGHTRED=`echo "\e[101m"`; LIGHTGREEN=`echo "\e[102m"`; LIGHTYELLOW=`echo "\e[103m"`; LIGHTBLUE=`echo "\e[104m"`; LIGHTPURPLE=`echo "\e[105m"`; LIGHTAQUA=`echo "\e[106m"`; WHITE=`echo "\e[107m"`; DEFAULT=`echo "\e[49m"`;

# Loop 1
# for filename in SH/*
# do
#     echo "${bold}${blink}${red}${filename}${normal} -----------------------------------------------------------------"
#     ls $filename
# done

# Loop 2
# for filename in *.txt
# do
#     echo "${bold}${blink}${BLUE}${white}${filename}${normal} -----------------------------------------------------------------"
#     echo ${lightblue}
#     cat $filename
#     echo ${normal}
# done

# Loop 3
# for filename in $(find . -type f -iname "*README*.txt")
# do
#     echo "${bold}${BLUE}${white}${filename}${normal} -----------------------------------------------------------------"
#     # echo ${lightblue}
#     # cat $filename
#     # echo ${normal}
# done

# Loop 4
# for i in $(seq $1)
# do
#         echo  "Iteration n: $i"     
# done

# Loop 5 - Back up all txt files
# for filename in $(find . -type f -iname "*.txt")
# do
#     cp $filename original-$filename
# done

