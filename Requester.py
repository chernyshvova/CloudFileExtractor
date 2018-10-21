import urllib.request
from connector.HTTPTools import get_http_request, check_http_request
from connector.proxy import proxy

class request_HTTPconnector:
    response = None
    proxy = None

    def __init__(self, proxy = None):
        if proxy:
            self.proxy = proxy

    def get_request(self, url):
        response = get_http_request(url)
        check_http_request(response)

    def set_request(self):
        pass
    def check_customeResponse(self):
        pass

    def reset_proxy(self, proxy):
        self.proxy = proxy
    

class web_Socket_Connector:
    def __init__(self, proxy = None):
        pass
    def send(self):
        pass
    def receive(self):
        pass
    def reset_proxy(self, proxy):
        pass
    def check_custom_response(self):
        pass