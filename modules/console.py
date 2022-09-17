from colorama import Fore, init;init()
import os, threading, time, json, keyboard, datetime, discord
from pystyle import *

config = json.load(open("./data/config.json"))
lock = threading.Lock()

class Console:

    @staticmethod
    def debug(content: str):
        if config['debug'] == True:
            if content != None:
                content = content.replace('[+]', f'[{Fore.LIGHTGREEN_EX} + {Fore.RESET}]{Fore.CYAN}').replace('[*]', f'[{Fore.LIGHTMAGENTA_EX} * {Fore.RESET}]{Fore.CYAN}').replace('[/]', f'[{Fore.CYAN} / {Fore.RESET}]{Fore.CYAN}').replace('[-]', f'[{Fore.RED} - {Fore.RESET}]{Fore.CYAN}')
                lock.acquire()
                print(f'[{Fore.CYAN}{datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")}{Fore.RESET}] [{Fore.CYAN}DEBUG{Fore.RESET}] {Fore.BLUE}〢{Fore.RESET} {content}{Fore.RESET}', flush=True)
                lock.release()
            else: pass
            
    @staticmethod
    def info(content: str):
        lock.acquire()
        content = content.replace('[+]', f'[{Fore.LIGHTGREEN_EX} + {Fore.RESET}]{Fore.CYAN}').replace('[*]', f'[{Fore.LIGHTMAGENTA_EX} * {Fore.RESET}]{Fore.CYAN}').replace('[/]', f'[{Fore.CYAN} / {Fore.RESET}]{Fore.CYAN}').replace('[-]', f'[{Fore.RED} - {Fore.RESET}]{Fore.CYAN}')
        print(f'[{Fore.CYAN}{datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}]  {Fore.BLUE}〢{Fore.RESET} {content}{Fore.RESET}', flush=True)
        lock.release()

    @staticmethod
    def printf(content: str):
        lock.acquire()
        print(content.replace('[+]', f'[{Fore.LIGHTGREEN_EX} + {Fore.RESET}]').replace('[*]', f'[{Fore.LIGHTYELLOW_EX} * {Fore.RESET}]').replace('[/]', f'[{Fore.CYAN} / {Fore.RESET}]').replace('[-]', f'[{Fore.RED} ✘ {Fore.RESET}]'))
        lock.release()


    @staticmethod
    def printe(content: str):
        lock.acquire()
        content = content.replace('[+]', f'[{Fore.LIGHTGREEN_EX} + {Fore.RESET}]{Fore.CYAN}').replace('[*]', f'[{Fore.LIGHTMAGENTA_EX} x {Fore.RESET}]{Fore.CYAN}').replace('[/]', f'[{Fore.CYAN} / {Fore.RESET}]{Fore.CYAN}').replace('[-]', f'[{Fore.RED} - {Fore.RESET}]{Fore.CYAN}')
        print(f'[{Fore.CYAN}{datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")}{Fore.RESET}] [{Fore.RED} ERROR {Fore.RESET}]  {Fore.GREEN}〢{Fore.RESET} {content}{Fore.RESET}', flush=True)
        lock.release()