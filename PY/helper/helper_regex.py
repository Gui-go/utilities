import re

string_lst = ['fun', 'dum', 'sun', 'gum']
x="I love to have fun."

print re.findall(r"(?=("+'|'.join(string_lst)+r"))",x)