from connector.HTTPTools import *
from connector.proxy import proxy

prx = proxy("1.20.102.58", 58461)
response = get_http_request_using_proxy("http://python-lab.ru/documentation/27/stdlib/unittest.html", prx)

print(str(response.getcode()))