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
    messagebox.showinfo("Orbit | Trolled", "GET TROLLED")




       
    
root = tk.Tk()
root.title("Orbit | VERSION: Trolled ")
root.configure(bg='red')
root.geometry("385x275")

# Label
my_label = Label(root, image=bg)
my_label.place(x=50, y=50, relwidth=1, relheight=1)



Information = Label(text = "TROLLED", font = 'Calbri')
Information.grid(row =1, column =1)
Usage = Label(text = 'You have been trolled...')
Usage.grid(row =2, column =1)
Website_Name = Label(text = "Access denied")
Website_Name.grid(row = 3, column =1)
Website = tk.Entry(root,bd = 5)
Website.grid(row =4, column =1)
Thread_Name = Label(text = "YOU FUCKING DUMBASS... no source code here...")
Thread_Name.grid(row = 5, column =1)
Thread = tk.Entry(root,bd = 5)
Thread.grid(row = 6, column =1)


Attack_Button = Button(text = '¿LMAFO?', font = 'Impact', bd = 5, command = Attack_Target)
Attack_Button.configure(bg='blue')

Attack_Button.grid(row = 7, column =1)

root.mainloop()
