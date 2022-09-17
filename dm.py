import os
import requests
from os.path import exists

dir_model = os.path.join("./data/model")
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

        