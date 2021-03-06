
from urllib.request import urlopen
from urllib import request
from connector.proxy import proxy
import socket
from urllib.error import HTTPError
from tqdm import tqdm
import requests
import math
from urllib.parse import quote_plus

def get_http_request(url):
    try:
        return urlopen(url)
    except socket.timeout as ex:
        print(str(ex) + "socked timeout")
    except HTTPError as ex:
        print(str(ex))
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")


def check_http_request(response):

    if response is None:
         raise Exception("response is empty")
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
        print(str(ex) + "---- socked timeou")
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")
        raise ex

def download_file(url, name, proxy = None):
    try:
        prx = None
        if proxy:
            prx = {proxy.host: proxy.port}
        response = requests.get(url, stream=True, timeout = 50, proxies = prx)
        total_size = int(response.headers.get('content-length', 0)); 
        block_size = 1024 * 1024
        with open(name, "wb") as handle:
            for data in tqdm(response.iter_content(block_size), total= math.ceil(total_size//block_size) , unit='MB', unit_scale=True):
                handle.write(data)
        print("done\n-----------------------------------------------------------------------")
    except socket.timeout as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")
    except Exception as ex:
        print(str(ex) + "---- TODO- instert error code in HTTPtools")


def urlEncode(url):
    return quote_plus(url)