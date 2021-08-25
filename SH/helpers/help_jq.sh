



# jq - Command-line JSON processor
# sudo apt-get install jq
# -c   (compact instead of pretty-printed output)
JsonData='[{"Book":"PHP 7"}, {"Publication":"Apress"}, {"Book":"React 16 Essentials"},{"Publication":"Packt"} ]'
echo $JsonData
echo "${JsonData}" | jq '.'
echo "${JsonData}" | jq -c  '.'
echo "${JsonData}" | jq -c  '.[]'

jq '.' SH/helpers/help_students.json
cat SH/helpers/help_students.json | jq '.' 
jq '.[] | .department' SH/helpers/help_students.json
jq '.[] | .name, .department' SH/helpers/help_students.json
jq 'map(del(.batch))' SH/helpers/help_students.json          # It's not permanent

jq 'map(.+10)' SH/helpers/help_numbers.json                  # Add 10 to each value
jq '.[2:4]' SH/helpers/help_colors.json                      # Closed/Open interval, as in JS
jq '.[:3]' SH/helpers/help_colors.json
jq '.[-3:]' SH/helpers/help_colors.json