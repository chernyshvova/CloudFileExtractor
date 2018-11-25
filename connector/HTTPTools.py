
from urllib.request import urlopen
from urllib import request
from connector.proxy import proxy
import socket
from tqdm import tqdm
import requests
import math

def get_http_request(url):
    try:
        return urlopen(url)
    except socket.timeout as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")

def check_http_request(response):
    if response.getcode()!= 200:
        raise Exception

#join with get_http_request
def get_http_request_using_proxy(url, proxy):
    try:
        req = request.Request(url)
        print(proxy.to_str())
        req.set_proxy(proxy.to_str(), "http")
        
        return urlopen(req, None, 10)
    except socket.timeout as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")

def download_file(url, name, proxy = None):
    try:
        prx = None
        if proxy:
            prx = {proxy.host: proxy.port}
        response = requests.get(url, stream=True, timeout = 10, proxies = prx)
        total_size = int(response.headers.get('content-length', 0)); 
        block_size = 1024
        with open(name, "wb") as handle:
            for data in tqdm(response.iter_content(block_size), total= math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
                handle.write(data)
    except socket.timeout as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")