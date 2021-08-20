#!/usr/bin/env python3

from colorama import Fore, Style


def info(string):
    info = "\t>> " + string
    return info

def done(string):
    done = Fore.GREEN + Style.BRIGHT + "[+] " + string
    return done

def running(string):
    running = Fore.YELLOW + Style.BRIGHT + "[!] " + string
    return running

def error(string):
    error = Fore.RED + Style.BRIGHT + "[-] " + string
    return error

def ask(string):
    ask = Fore.BLUE + Style.BRIGHT + "[?] " + string
    return ask

def normal_text():
    print(Style.RESET_ALL)

def white(string):
    white = Fore.WHITE + Style.BRIGHT + string
    return white

def magenta(string):
    magenta = Fore.MAGENTA + Style.BRIGHT + string
    return magenta

def cyan(string):
    cyan = Fore.CYAN + Style.BRIGHT + string
    return cyan