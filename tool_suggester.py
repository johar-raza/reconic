#!/usr/bin/env python3

import sys
from cprint import *
from subprocess import call
from __settings import THREADS,WORDLIST


def dirsearch():
    dirsearch = "dirsearch -u {url} -w {wordlist} -x 400,500 -r -t {threads}".format(url=target, wordlist=WORDLIST, threads=THREADS).split(" ")
    call(dirsearch)
    
    
def nikto():
    nikto = "nikto -a {}".format(target).split(" ")
    call(nikto)


def list_shares():
    shares = "smbclient -L \\\\{}".format(target).split(" ")
    call(list_shares)
    
    
def enum4linux():
    enum4linux = "enum4linux -a {}".format(target).split(" ")
    call(enum4linux)


def tool_suggester():
    print(white("Which port would you like to enumerate?"))
    for port in discovered_ports:
        print(white("Port [{}]").format(port))
    
    inp = input("\n[>] Option: ")
    
    if int(inp) == 80:
        print("\n[1] Brute-force directories (Dirsearch)")
        print("[2] Fire up Nikto")
        print("[3] Enumerate another port")
        
        inp = input("[>] Option: ")
        
        if int(inp) == 1:
            dirsearch()
        elif int(inp) == 2:
            nikto()
        elif int(inp) == 3:
            tool_suggester()
        else:
            print(error("Invalid option."))
            sys.exit()
    
    elif int(inp) == 445 or int(inp) == 139:
        print("\n[1] List SMB shares (Smbclient)")
        print("[2] Start Enum4Linux")
        print("[3] Enumerate another port")
        
        inp = input("[>] Option: ")
        
        if int(inp) == 1:
            list_shares()
        elif int(inp) == 2:
            enum4linux()
        elif int(inp) == 3:
            tool_suggester()
        else:
            print(error("Invalid option."))
            sys.exit()

    else:
        print(error("Invalid port!"))
    


if __name__=="__main__":
    target = "8.8.8.8"
    discovered_ports = [80, 139, 445]
    tool_suggester()