import os
import subprocess
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
print(colored("\t                       __                __","cyan"))
print(colored("\t    ____  __  __      / /_  __  ______  / /_","cyan"))
print(colored("\t   / __ \/ / / /_____/ __ \/ / / / __ \/ __/","cyan"))
print(colored("\t  / /_/ / /_/ /_____/ / / / /_/ / / / / /_","cyan"))
print(colored("\t / .___/\__, /     /_/ /_/\__,_/_/ /_/\__/","cyan"))
print(colored("\t/_/    /____/","cyan"))
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
print(colored(" __   __   __  ___     __   __                  ___  __","magenta"))  
print(colored("|__) /  \ |__)  |     /__` /  `  /\  |\ | |\ | |__  |__)","magenta"))
print(colored("|    \__/ |  \  |     .__/ \__, /~~\ | \| | \| |___ |  \ ","magenta"))
print('')
subprocess.run(["/usr/bin/nmap", "-sC", "-sV","-p-", s_ip])
print(colored("_"*80,"red"))

# for finding hidden web directories
print(colored("[*] Scanning Hidden Web Directories...","yellow"))
print('')

print(colored("      ___  __      __   __                  ___  __ ","magenta"))
print(colored("|  | |__  |__)    /__` /  `  /\  |\ | |\ | |__  |__)","magenta"))
print(colored("|/\| |___ |__)    .__/ \__, /~~\ | \| | \| |___ |  \ ","magenta"))
print('')
print(os.system("%s%s %s" % ("/usr/bin/gobuster -q dir -u http://",s_ip,"-w /usr/share/SecLists/Discovery/Web-Content/big.txt -x .txt -x .php -x .js -x .html")))
print('')
print(colored("_"*80,"red"))

#smb
try:
        
        print(colored(" __         __      ___                 ","magenta"))
        print(colored("/__`  |\/| |__)    |__  |\ | |  |  |\/|","magenta"))
        print(colored(".__/  |  | |__)    |___ | \| \__/  |  |","magenta")) 
        print('')
        print(colored("[*] Scanning the SMB services: ","yellow"))
        print('')
        subprocess.run(["enum4linux", s_ip])
        print(colored("_"*80,"red"))
except Exception as e:
        print(str(e))
# whois

print(colored("[*] Whois information: ","yellow"))
print(colored("           __  @  __ ","magenta"))
print(colored("|  | |__| /  \ | /__`","magenta"))
print(colored("|/\| |  | \__/ | .__/","magenta"))
 
print('')
print(os.system("%s %s " % ("whois " , s_ip )))
print('')
print(colored("scanning complete!","yellow",attrs=['reverse','blink']))
print(colored("="*80,"red"))
