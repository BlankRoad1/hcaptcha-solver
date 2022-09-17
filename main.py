import os
from modules.captcha import CaptchaSolver
import random
from datetime import datetime
from modules.console import Console



# discord
website_key_captcha="4c672d35-0701-42b2-88c3-78380b0db560"
website_URL_captcha="http://discord.com"


proxypath = "./data/proxies.txt"
proxy = open(proxypath,"r").read().split("\n")

clear = True
count = 1
while True:
    if open(proxypath,"r").read() == '':
                proxys = ""
    else:
        proxys = random.choice(proxy)
        
    if clear == True:
        os.system('cls')
        clear = False


    Console.info(str(count)+ " Proxy Selected: "+proxys)
    try:
        start = datetime.now()
        start_time = start.strftime("%H:%M:%S")

        #call captcha here
#===============================================================================================================        
        #this is your jackpot line
        token = CaptchaSolver.get_captcha_by_ai(website_key_captcha, website_URL_captcha ,proxys)
#===============================================================================================================        
        
        end = datetime.now()

        end_end = end - start
        Console.info("Total Time Taken = " + str(end_end.seconds) + " seconds")
        if token == None:
            Console.printe("Captcha Error, Retrying...")
        else:
            Console.info("Token: "+token)
    except Exception as e:
        if "Max retries exceeded" in str(e):
            Console.printe("Max Retries reached, Changing proxy...")
        else:
            print(e)
    count +=1
 
