#!/usr/bin/env python3

import subprocess
from cprint import done, error, normal_text, running

def ping(target):
    """
    Returns True if host (str) responds to a ping request.
    A host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    print(running("Pinging target"))
    normal_text()
    # Building the command. Ex: "ping -c 1 x.x.x.x"
    command = ['ping', '-c', '1', target]

    response = subprocess.call(command)
    
    if response != 0:
        print(error("Target seems down!\n"))
    else:
        print("\n")
        print(done("Target is up!\n"))
    
    return response