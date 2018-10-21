
from urllib.request import urlopen
from urllib import request
from connector.proxy import proxy
import socket

def get_http_request(url):
    try:
        return urlopen(url)
    except Exception:
        print("invalid url---- TODO- instert error code in HTTPtools")

def check_http_request(response):
    if response.getcode()!= 200:
        raise Exception

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