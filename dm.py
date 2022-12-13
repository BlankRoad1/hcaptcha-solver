import os
import requests
from os.path import exists

dir_model = os.path.join("./data/model")
dir_objects = os.path.join("./modules/ai_finder/objects.yaml")


print("If any error caused while processing, you have to do the following steps manually: ")
print("1. Goto https://api.github.com/repos/QIN2DIM/hcaptcha-challenger/releases and download all the files. \n2. Create a folder model in data and paste them in model folder.\n3. Goto https://raw.githubusercontent.com/QIN2DIM/hcaptcha-challenger/main/src/objects.yaml\n4. Copy all content from 'seaplane:' till end and paste them in ./modules/ai_finder/objects.yaml file.")
print("." * 50)

# #==============================================================================
#----------------------- Download models in model folder

print("Download all AI Files...")
r = requests.get(
    "https://api.github.com/repos/QIN2DIM/hcaptcha-challenger/releases")
for asset in r.json()[0].get("assets"):
    url = asset.get("browser_download_url")
    name = asset.get("name")
    path = os.path.join(dir_model, name)
    file_exists = exists(path)

    if name == "rainbow.yaml":
        #rainbow file gets updated everytime
        os.makedirs(dir_model, exist_ok=True)
        if not url.lower().startswith("http"):
            raise ValueError from None
        print(f"Downloading {name} from {url}")
        with requests.get(url, stream=True) as response, open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

    if file_exists == False:

        os.makedirs(dir_model, exist_ok=True)
        if not url.lower().startswith("http"):
            raise ValueError from None
        print(f"Downloading {name} from {url}")
        with requests.get(url, stream=True) as response, open(path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

print("$" * 50)

#==============================================================================
#----------------------- Download objects in objects.yaml file 


print("Now Updating Objects.yaml File [can be found in modules>ai_finder]")

#read file objects.yaml
current_ObjectYaml = open(dir_objects,encoding="utf-8").read().splitlines()
modifedV = current_ObjectYaml


#read from the link
objects_QIN2DIM = requests.get("https://raw.githubusercontent.com/QIN2DIM/hcaptcha-challenger/main/src/objects.yaml").text.split("\n")

#some useless variables
index_curr_object = 0
index_qin2dim_objects = 0

update = False

if current_ObjectYaml[len(current_ObjectYaml) - 1].isspace(): 
    print("Last line of objects.yaml should not be empty")


elif current_ObjectYaml[len(current_ObjectYaml) - 1] != objects_QIN2DIM[len(objects_QIN2DIM) - 1]:
    #get last objects of current_ObjectYaml and objects_QIN2DIM
    object_Q = objects_QIN2DIM[len(objects_QIN2DIM) - 1]
    object_C = current_ObjectYaml[len(current_ObjectYaml) - 1]

    #default size of objects.yaml file
    if len(current_ObjectYaml) <= 69:

        #get index of both
        for idx, line in enumerate(current_ObjectYaml):
            if object_C in line:
                    index_curr_object = idx
                    print("Start Index Current Object: ",idx,"| Value: ", line)

        for idx, line in enumerate(current_ObjectYaml):
            if "label_alias:" in line:
                    index_qin2dim_objects = idx + 1
                    print("Start Index QIN2DIM Object: ",idx,"| Value: ", line)
        
        # compare both arrays
        for O in range(len(current_ObjectYaml)):
            if O >= index_curr_object:

                for Q in range(len(objects_QIN2DIM)):
                    if Q >= index_qin2dim_objects:
                        
                        #lets compare each line of both
                        if objects_QIN2DIM[Q] != current_ObjectYaml[O]:
                            modifedV.append(objects_QIN2DIM[Q])
                            update = True
                            print("Adding New Object: ",objects_QIN2DIM[Q])
#***********************************************************************    
    else:
        #get index of both
        for idx, line in enumerate(current_ObjectYaml):
            if object_C.strip() in line:
                    index_curr_object = idx
                    # print("Start Index Current Object: ",idx,"| Value: ", line)

        for idx, line in enumerate(objects_QIN2DIM):
            temp = object_C.strip()
            if  temp in line:
                    index_qin2dim_objects = idx + 1
                    # print("Start Index QIN2DIM Object: ",idx,"| Value: ", line)
        
        # compare both arrays
        for O in range(len(current_ObjectYaml)):
            if O >= index_curr_object:

                for Q in range(len(objects_QIN2DIM)):
                    if Q >= index_qin2dim_objects:
                        
                        #lets compare each line of both
                        if objects_QIN2DIM[Q] != current_ObjectYaml[O]:
                            modifedV.append(objects_QIN2DIM[Q])
                            update = True
                            print("Adding New Object: ",objects_QIN2DIM[Q])

    with open(dir_objects, "w",encoding="utf-8") as final_output:
        for i,line in enumerate(modifedV,1):         
                final_output.writelines("\n"+line)
        if update == True:
            print("Updated Objects.yaml")        
        else:
            print("Nothing to update in Objects.yaml")
            
else:
    print("Nothing to update in Objects.yaml")
