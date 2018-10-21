from connector.HTTPTools import *
from connector.proxy import proxy

from urllib import request
from tqdm import tqdm
import requests
#request.urlretrieve('https://drive.google.com/uc?authuser=0&id=0B6kd31lscJ9TdmVadEd6ZGc0NTQ&export=download', './ложим_в_текущаю_папку.png')


#url = "https://drive.google.com/uc?authuser=0&id=0B6kd31lscJ9TdmVadEd6ZGc0NTQ&export=download"
#response = requests.get(url, stream=True)
#with open("10MB", "wb") as handle:
    #for data in tqdm(response.iter_content()):
        #handle.write(data)
#print(str(response.getcode()))

download_file("https://drive.google.com/uc?authuser=0&id=0B6kd31lscJ9TdmVadEd6ZGc0NTQ&export=download", "pic2.png")