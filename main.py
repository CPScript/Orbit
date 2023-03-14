import time
from subprocess import call
import os
from os import system
from platform import platform

# delete
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)
print("Downloading Dependancies in 10 seconds")
print("Please wait...")
time.sleep(10)

# Installs requirments
os.system(delet)
os.system('pip install -r requirements.txt')
os.system(delet)
call(["python", "tool/Install.py"])
os.system(delet)


#loading screen
print("Loading.")
time.sleep(1)
os.system(delet)
print("Loading..")
time.sleep(1)
os.system(delet)
print("Loading...")
time.sleep(1)
os.system(delet)
print("Loading.")
time.sleep(1)
os.system(delet)
print("Loading..")
time.sleep(1)
os.system(delet)
print("Loading...")
time.sleep(1)
os.system(delet)
print("Loading.")
time.sleep(1)
os.system(delet)
print("Loading..")
time.sleep(1)
os.system(delet)
print("Loading...")
time.sleep(1)
os.system(delet)

print("Done!")
time.sleep(1)
os.system(delet)
print("Please choose what to use> 1 or 2")
print("<1> Terminal [recemended]")
print("<2> GUI")
print(" ")
print(" ")
print("Your Choice:")
choice = input("")


if choice == "1":
    os.system(delet)
    print("Loading.")
    time.sleep(1)
    os.system(delet)
    print("Loading..")
    time.sleep(1)
    os.system(delet)
    print("Loading...")
    time.sleep(1)
    os.system(delet)
    print("Loading.")
    time.sleep(1)
    os.system(delet)
    print("Loading..")
    time.sleep(1)
    os.system(delet)
    print("Loading...")
    time.sleep(1)
    os.system(delet)
    print("Done!")
    time.sleep(5)
    call(["python", "tool/DDoS.py"])

      
      
if choice == "2":
    os.system(delet)
    print("Loading.")
    time.sleep(1)
    os.system(delet)
    print("Loading..")
    time.sleep(1)
    os.system(delet)
    print("Loading...")
    time.sleep(1)
    os.system(delet)
    print("Loading.")
    time.sleep(1)
    os.system(delet)
    print("Loading..")
    time.sleep(1)
    os.system(delet)
    print("Loading...")
    time.sleep(1)
    os.system(delet)
    print("Done!")
    time.sleep(5)
    call(["python", "tool/GUI.py"])
