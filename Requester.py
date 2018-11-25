import urllib
from urllib import request
from connector.HTTPTools import get_http_request, check_http_request, get_http_request_using_proxy, download_file
from connector.proxy import proxy

class connector:
    response = None

    def get_http_request(self, url, proxy = None):
        if proxy == None:
            self.response = get_http_request(url)
        else:
            self.response = get_http_request_using_proxy(url, proxy)
    
        check_http_request(self.response)
    
    def get_body(self):
        return self.response.read()

    def download_file(self, url, name):
        download_file(url, name, None)