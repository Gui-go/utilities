#!/bin/bash

# Notes:
# jq - Command-line JSON processor
# sudo apt-get install jq

url="http://wttr.in/?format=j1"
json="$(wget -qO- "$url")"
 
#color library
bold=`echo -en "\e[1m"`; underline=`echo -en "\e[4m"`; dim=`echo -en "\e[2m"`; strickthrough=`echo -en "\e[9m"`; blink=`echo -en "\e[5m"`; reverse=`echo -en "\e[7m"`; hidden=`echo -en "\e[8m"`; normal=`echo -en "\e[0m"`; black=`echo -en "\e[30m"`; red=`echo -en "\e[31m"`; green=`echo -en "\e[32m"`; orange=`echo -en "\e[33m"`; blue=`echo -en "\e[34m"`; purple=`echo -en "\e[35m"`; aqua=`echo -en "\e[36m"`; gray=`echo -en "\e[37m"`; darkgray=`echo -en "\e[90m"`; lightred=`echo -en "\e[91m"`; lightgreen=`echo -en "\e[92m"`; lightyellow=`echo -en "\e[93m"`; lightblue=`echo -en "\e[94m"`; lightpurple=`echo -en "\e[95m"`; lightaqua=`echo -en "\e[96m"`; white=`echo -en "\e[97m"`; default=`echo -en "\e[39m"`; BLACK=`echo -en "\e[40m"`; RED=`echo -en "\e[41m"`; GREEN=`echo -en "\e[42m"`; ORANGE=`echo -en "\e[43m"`; BLUE=`echo -en "\e[44m"`; PURPLE=`echo -en "\e[45m"`; AQUA=`echo -en "\e[46m"`; GRAY=`echo -en "\e[47m"`; DARKGRAY=`echo -en "\e[100m"`; LIGHTRED=`echo -en "\e[101m"`; LIGHTGREEN=`echo -en "\e[102m"`; LIGHTYELLOW=`echo -en "\e[103m"`; LIGHTBLUE=`echo -en "\e[104m"`; LIGHTPURPLE=`echo -en "\e[105m"`; LIGHTAQUA=`echo -en "\e[106m"`; WHITE=`echo -en "\e[107m"`; DEFAULT=`echo -en "\e[49m"`;

description=$(echo $json|jq -r ."current_condition[0]|(.weatherDesc[0].value)")
# tempF=$(echo $json|jq -r ."current_condition[0]|(.temp_F)")
tempC=$(echo $json|jq -r ."current_condition[0]|(.temp_C)")
humidity=$(echo $json|jq -r ."current_condition[0]|.humidity")
localObsDateTime=$(echo $json|jq -r ."current_condition[0]|(.localObsDateTime)" | cut -d " " -f 2,3)
# cc0=$(echo $json|jq -r ."current_condition[0]") 

if [[ ${tempC} > 40 ]]
then
  color=${red}
elif [[ ${tempC} > 20 ]]
then
  color=${orange}
elif [[ ${tempC} < 20 ]]
then
  color=${blue}
else
  color=""
fi

# red=`echo -en "\e[31m"`
# color=$red
 
echo "It is currently ${description}"
# echo "Temperature: ${temp}℉"
echo "Temperature: ${color}${tempC}C${normal}"
echo "Humidity: ${humidity}%"
echo "${bold}last local time registery: ${localObsDateTime}${normal}"
echo 
# echo "current_condition[0]: \n ${cc0}"

# Run with bash command