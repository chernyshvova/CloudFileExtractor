
from urllib.request import urlopen

def get_http_request(url):
    try:
        return urlopen(url)
    except Exception:
        print("invalid url---- TODO- instert error code in HTTPtools")