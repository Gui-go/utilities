#!/binbash

echo "Now executing $0 to pratice commands"

echo
echo "Lorem ipsum dolor sit amet" | cut -d ' ' -f 1,2
echo "Lorem ipsum dolor sit amet" | cut -d ' ' -f 1,2 --output-delimiter='_'

echo
echo "$ cat SH/helpers/help.txt | sed -n '3,4p'"
cat SH/helpers/help.txt | sed -n '3,4p'

echo 
echo "$ sed -n '3,4p' SH/helpers/help.txt"
sed -n '3,4p' SH/helpers/help.txt

echo 
echo "$ sed -n '4p' SH/helpers/help.txt | cut -d "," -f 2,3,4"
sed -n '4p' SH/helpers/help.txt | cut -d "," -f 2,3,4

echo 
echo "$ sed -n '4p' SH/helpers/help.txt | cut -d "," -f 2,3,4 | tr -d ",""
sed -n '4p' SH/helpers/help.txt | cut -d "," -f 2,3,4 | tr -d ","

echo 
getent passwd | cut -d ':' -f1 # Get a list of all users

echo 
cut -d , -f 2 animals.csv # Gets second column of animals.csv
cut -d , -f 1 SH/helpers/help_animals.csv # Gets first column
cut -d , -f 2 SH/helpers/help_animals.csv | sort | uniq
cut -d , -f 2 SH/helpers/help_animals.csv | sort | uniq -c # Counts how many times an animal accours





