import json
import os
import numpy as np
from random import randint
from time import time
from PIL import Image
from requests import get

def dump_json(data):
    return json.dumps(data)

def get_image_data(img_url):
    if img_url.lower().startswith("https://"):
        r = get(img_url, allow_redirects=True)
        file_name = str(time()) + str(randint(1, 655687656768)) + "." + img_url.split(".")[-1]

        try:
            os.mkdir("data")
        except:
            pass
        with open("data/" + file_name, 'wb') as f:
            f.write(r.content)
        img_url = "data/" + file_name

    img_data = Image.open(img_url)
    return img_data

def preprocess_malaria(img_data, width=64, height=64):
    # Accuracy - 97.0625%
    img_data = img_data.convert("RGB")
    img_data = img_data.resize((height, width))
    img_raw = np.array(img_data) / 255 / 255

    return img_raw

def preprocess_skin_cancer(img_data, width=224, height=224):
    # Accuracy - 89.697%
    img_data = img_data.convert("RGB")
    img_data = img_data.resize((height, width))
    img_raw = np.array(img_data) / 255

    return img_raw
