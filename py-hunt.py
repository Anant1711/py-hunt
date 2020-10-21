import os
import time
import datetime
import socket
from urllib.request import urlopen 
from termcolor import colored



#banner
print(colored("="*80,"red"))
print("                    ________           ")
print("                  _/        \_          ")
print("                 /            \         ")
print("                |              |            ")
print("                |,  .-.  .-.  ,|           ")
print("                | )(__/  \__)( |                ")
print("                |/     /\     \|                 ")
print("      (@_       (_     ^^     _)              ")
print(" _     ) \_______\__|######|__/____________________________________ ")
print("(_)@8@8@8{}_______|-\######/-|____"+(colored("By Anant","yellow",attrs=['reverse'])+("________________________/ ")))
print("       )_/        \          / ")
print("      (@           `--------`  ")
print('')
print(colored("                       __                __","cyan"))
print(colored("    ____  __  __      / /_  __  ______  / /_","cyan"))
print(colored("   / __ \/ / / /_____/ __ \/ / / / __ \/ __/","cyan"))
print(colored("  / /_/ / /_/ /_____/ / / / /_/ / / / / /_","cyan"))
print(colored(" / .___/\__, /     /_/ /_/\__,_/_/ /_/\__/","cyan"))
print(colored("/_/    /____/","cyan"))
print('')
print(colored("="*80,"red"))
time.sleep(3)
print(datetime.datetime.now())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = (input(colored("Enter the IP: ","yellow")))
s_ip = socket.gethostbyname(ip)
print(colored(s_ip,"green"))
print(colored("Scanning start:  ","yellow"))
time.sleep(2)

# namp scanning start
print(colored("_"*80,"red"))
print(colored("[*] Scanning the ports and services: ","yellow"))
print('')
print(os.system("%s %s" % ("nmap -sC -sV -p-",s_ip)))
print(colored("_"*80,"red"))

# for finding hidden web directories
print(colored("[*] Scanning Hidden Web Directories...","yellow"))
print('')
print(os.system("%s%s %s" % ("gobuster -q dir -u http://",s_ip,"-w /usr/share/SecLists/Discovery/Web-Content/big.txt -x .txt -x .php -x .js -x .html"))) 
print(colored("scanning complete!","yellow",attrs=['reverse','blink']))
print(colored("="*80,"red"))
