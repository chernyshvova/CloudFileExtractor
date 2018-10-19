from connector.HTTPTools import *

response = get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")

print(str(response.getcode()))