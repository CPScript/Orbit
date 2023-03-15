import time
import subprocess
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

# Disclamer
print("By all means, CPScript or anyother creators are not responsible with what the user (YOU) does with this tool, all blame is on the user (YOU) and if you get cought you agree that your at fault...")
print(" ")
print("------question------")
print("[+] By typing '1' you agree to these conditions, and will be given access to this tool.")
print("[+] By typing '2' you Dont agree.")
choice = input("")


if choice == "1":
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
    print("Please choose what to use - 1 or 2")
    print("[1] - Orbit Terminal [Recemended] [Not the most reliable]")
    print("[2] - Orbit app [Easy 2 Use] [Payed 4]")
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
        print("How to get the 'Orbit' application:")
        print(" ")
        print(" ")
        print("The app will costs money...")
        print("To buy the 'Orbit' app follow these steps")
        print(" ")
        print("-----Steps-----")
        print("Message this user on Discord - Orbit#1654")
        print("You will then wait untill i can get your message.")
        print("Once gotten to, I will then send you a Bitcoin wallet link.")
        print("You will send the sum of money to the wallet")
        print("Once payments are confirmed i will send you your .zipped folder (password protected)")
        print("I will then send you your personal password to unlock that folder")
        print("All you will then have to do is extract and run the 'orbit app'")
        print("-----Steps-----")
        print(" ")
        print("Tool will cost more $$$ the more its updated, its a one time purchase for the version you want... then its yours")
        print("There will be no updates, you will have to buy newer versions")
        print("You can buy this as many times as you want.")
        

       


if choice == "2":
    os.system(delet)
    print("Orbit: <-0->")
    print("encrypting program files...")
    time.sleep(2)
    print("This will not harm your computer in any way.")
    subprocess.call([r'tool/encrypt.vbs'])

