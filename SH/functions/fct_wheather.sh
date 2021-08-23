#!/bin/bash


# jq - Command-line JSON processor
# sudo apt-get install jq

url="http://wttr.in/?format=j1"
json="$(wget -qO- "$url")"
 
#color library
bold=`echo "\e[1m"`; underline=`echo "\e[4m"`; dim=`echo "\e[2m"`; strickthrough=`echo "\e[9m"`; blink=`echo "\e[5m"`; reverse=`echo "\e[7m"`; hidden=`echo "\e[8m"`; normal=`echo "\e[0m"`; black=`echo "\e[30m"`; red=`echo "\e[31m"`; green=`echo "\e[32m"`; orange=`echo "\e[33m"`; blue=`echo "\e[34m"`; purple=`echo "\e[35m"`; aqua=`echo "\e[36m"`; gray=`echo "\e[37m"`; darkgray=`echo "\e[90m"`; lightred=`echo "\e[91m"`; lightgreen=`echo "\e[92m"`; lightyellow=`echo "\e[93m"`; lightblue=`echo "\e[94m"`; lightpurple=`echo "\e[95m"`; lightaqua=`echo "\e[96m"`; white=`echo "\e[97m"`; default=`echo "\e[39m"`; BLACK=`echo "\e[40m"`; RED=`echo "\e[41m"`; GREEN=`echo "\e[42m"`; ORANGE=`echo "\e[43m"`; BLUE=`echo "\e[44m"`; PURPLE=`echo "\e[45m"`; AQUA=`echo "\e[46m"`; GRAY=`echo "\e[47m"`; DARKGRAY=`echo "\e[100m"`; LIGHTRED=`echo "\e[101m"`; LIGHTGREEN=`echo "\e[102m"`; LIGHTYELLOW=`echo "\e[103m"`; LIGHTBLUE=`echo "\e[104m"`; LIGHTPURPLE=`echo "\e[105m"`; LIGHTAQUA=`echo "\e[106m"`; WHITE=`echo "\e[107m"`; DEFAULT=`echo "\e[49m"`;

description=$(echo $json|jq -r ."current_condition[0]|(.weatherDesc[0].value)")
# tempF=$(echo $json|jq -r ."current_condition[0]|(.temp_F)")
tempC=$(echo $json|jq -r ."current_condition[0]|(.temp_C)")
humidity=$(echo $json|jq -r ."current_condition[0]|.humidity")
localObsDateTime=$(echo $json|jq -r ."current_condition[0]|(.localObsDateTime)" | cut -d " " -f 2,3)

cc0=$(echo $json|jq -r ."current_condition[0]") 
 
if [[ ${tempC} > 40 ]]
then
  color=${red}
elif [[ ${tempC} > 25 ]]
then
  color=${orange}
elif [[ ${tempC} < 10 ]]
then
  color=${blue}
else
  color=""
fi
 
# echo "It is currently ${bold}${description}${normal}"
# echo "${color}Temperature: ${temp}℉ ${default}"
# echo "Humidity: ${humidity}%"

echo "It is currently ${description}"
# echo "Temperature: ${temp}℉"
echo "Temperature: ${color}${tempC}C${normal}"
echo "Humidity: ${humidity}%"
echo "${bold}last local time registery: ${localObsDateTime}${normal}"
echo 
echo "current_condition[0]: \n ${cc0}"

# echo $json|jq -r .