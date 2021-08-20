#!/usr/bin/env python3

import sys
import socket
import threading

from queue import Queue
from colorama import Style
from datetime import datetime
from cprint import *


def portscanner(target):
    
    def scan_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            conx = s.connect((t_ip,port))
            with print_lock:
                print(magenta("Port {}".format(port)) + Style.RESET_ALL + " is open")
                discovered_ports.append(str(port))
            conx.close()
        except (ConnectionRefusedError, AttributeError, OSError):
            pass


    def threader():
        while(1):
            worker = q.get()
            scan_port(worker)
            q.task_done()

    
    socket.setdefaulttimeout(0.30)
    discovered_ports = []
    print_lock = threading.Lock()

    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print(error("Invalid format\n"))
        sys.exit()

    print(running("Scanning all ports"))
    t1 = datetime.now()
    normal_text()

    q = Queue()

    for x in range(200):
        t = threading.Thread(target = threader, daemon=True)
        t.start()

    for worker in range(1,65536):
        q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1

    print("\n")
    print(done("Port scan completed in " + str(total).split(".")[0] + "\n"))
    normal_text()
    
    return discovered_ports

if __name__ == "__main__":
    target = input("Enter IP address or URL: ")
    portscanner(target)
