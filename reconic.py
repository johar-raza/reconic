#!/usr/bin/env python3

from datetime import date, datetime
import os
from posixpath import commonpath
import re
import sys
import subprocess

from cprint import *
from pinger import ping
from portscanner import portscanner


def banner():
    subprocess.call('clear', shell=True)
    
    banner = r"""
 ______     ______     ______     ______     __   __     __     ______
/\  == \   /\  ___\   /\  ___\   /\  __ \   /\ "-.\ \   /\ \   /\  ___\
\ \  __<   \ \  __\   \ \ \____  \ \ \/\ \  \ \ \-.  \  \ \ \  \ \ \____
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\\"\_\  \ \_\  \ \_____\
  \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_/   \/_____/


    """
    print(white(banner))
    print(info("Version: 0.1"))
    print(info("Created by Joras3c\n\n"))
    normal_text()


def validate_ip(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    
    if(re.search(regex, ip)):
        return ip
    else:
        return "Invalid IP address"


def enter_ip():
    print(white("-"*75))
    ip = input("[>] Enter IP address: ")
    #print("-"*75 + "\n")
    print("\n")
    normal_text()
    return validate_ip(ip)


def choice_one(scan):
    normal_text()
    print(white("What would you like to do:"))
    print("[1] Run the recommended nmap scan")
    print("[2] Scan another target")
    print("[3] Exit to console\n")
    
    option = input("[>] Option: ")
    normal_text()
    
    if option == "1":
        nmap(scan)
    elif option == "2":
        reconic()
    elif option == "3":
        print("Bye bye!")
        sys.exit()
    else:
        print(error("Invalid option!"))
        choice_one(scan)


def nmap(scan):
    print(running("Starting nmap"))
    normal_text()
    nmap_dir = scan.split(" ")[-2].split("scan")[0]
    target_dir = nmap_dir.split("/")[0]
    
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)    
    if not os.path.exists(nmap_dir):
        os.mkdir(nmap_dir)
    
    command = scan.split(" ")
    
    t1 = datetime.now()
    subprocess.call(command)
    t2 = datetime.now()
    total = t2 - t1
    
    print("\n")
    print(done("Nmap finished in " + str(total).split(".")[0] + "\n"))
    normal_text()


def reconic():
    target = enter_ip()
    
    if target == "Invalid IP address":
        print(error("Invalid IP address\n"))
    else:
        discovered_ports = portscanner(target)
        recommended_scan = "nmap -p{ports} -sV -sC -T4 -Pn -oA {ip}/nmap/scan {ip}".format(ports=",".join(discovered_ports), ip=target)
        print(running("Recommended nmap scan:\n"))
        print("    " + recommended_scan)
        
        choice_one(recommended_scan)


if __name__=='__main__':
    banner()
    reconic()