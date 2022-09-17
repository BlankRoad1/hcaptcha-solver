import json, time, httpx, cv2, os, json, base64
import tensorflow as tf
from keras.models import load_model
tf.debugging.disable_traceback_filtering()
import numpy as np
from . import hcaptcha
from .console import Console
import requests

from modules.ai_finder.solutions import  resnet, yolo
from pathlib import Path


path_objects_yaml = './modules/ai_finder/objects.yaml'

dir_model = './data/model'
label_alias = {}

# Automatic registration
pom_handler = resnet.PluggableONNXModels(path_objects_yaml)
#Update labelalias list
label_alias.update(pom_handler.label_alias['en'])
on_rainbow = True
pluggable_onnx_models = pom_handler.overload(dir_model, on_rainbow)

class CaptchaSolver:
    def switch_solution(label):
        global pluggable_onnx_models
        global yolo_model
        global label_alias 
        label_alias1 = label_alias.get(label)
        
        # Select ONNX model - ResNet | YOLO
        if pluggable_onnx_models.get(label_alias1):
            return pluggable_onnx_models[label_alias1]
        return "n"

    def challenge(model, alias, label):
            global pluggable_onnx_models
            global yolo_model
            global label_alias 
            mypath  = "./data/captcha_temp_images"
            count = 0

            # {{< IMAGE CLASSIFICATION >}}
            with open(mypath+"/"+alias+".png", "rb") as file:
                data = file.read()
            result = None
            #AI PART from hcaptcha-challenger
            result = model.solution(img_stream=data, label=label_alias[label])
            return result
            
    @staticmethod
    def get_captcha_by_ai(siteky, host ,proxy: str):
        Console.debug("[*] SOLVING...")
        ch = hcaptcha.Challenge(
            sitekey=siteky,
            page_url=host,
            http_proxy=proxy
        )

        if ch.token:
            return ch.token
        label = ""
        if ch.question:
            Console.debug("[*] Question: "+ch.question)
            question = ch.question
            if "Please click each image containing an" in question:
                question = question.replace("Please click each image containing an ","")
            elif "Please click each image containing a" in question:
                question = question.replace("Please click each image containing a ","")
            else:
                question = question.replace("Please click each image containing","")
            label = question.replace(".","")
        answers = []
        count = 0
        for tile in ch.tasks:

            ### Downlowds hcaptcha images, wrote the code for testing the new models.            
            url = tile.url
            # Console.debug(f"[-] Stored Image ")
            req = requests.get(url, stream = True)
            with open("./data/captcha_temp_images/"+ "image_" +str(count) + ".png", 'wb') as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            #alias will be our file name                        
            alias = "image_" +str(count)                    
            count +=1

            solution = CaptchaSolver.switch_solution(label)
            if solution != "n" or result != None:                
                result = CaptchaSolver.challenge(solution,alias, label)
                #True means correct, false means wrong image
                Console.debug(f"[+] Image Name: {alias}, Result: {result}")
            else:
                Console.info(f"[+] AI not trained for this captcha type yet !!!")
                break
            if result == True:
                answers.append(tile)
        try:
            Console.debug(f"[+] Solving Captcha by Choosing Images Now.")
            token = ch.solve(answers)
            Console.debug(f"[*] Deleting Images which i downloaded")
            [f.unlink() for f in Path("./data/captcha_temp_images/").glob("*") if f.is_file()] 
            return token
        except hcaptcha.ApiError as e:
            # print("Api Error")

            #This is where the captcha fails. means its solved but wrong images are chosen
            Console.debug(f"[-] Captcha solved but wrong, Retrying...")

            
