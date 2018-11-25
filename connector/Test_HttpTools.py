from HTTPTools import *
import unittest
from proxy import proxy
import os

class HTTPToolsTests(unittest.TestCase):
    def test_correct_queryWithoutExceptions(self):
        get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")

    def test_correct_response(self):
        response = get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")
        self.assertEqual(200, response.getcode())

    def test_wrong_url(self):
        response = get_http_request("dasdadasdsadas")
        self.assertEqual(None, response)

    def test_check_wrong_response_and_throw_exception(self):
        response = get_http_request("dsadadsads")
        with self.assertRaises(Exception):
            check_http_request(response)

    def test_check_correct_response_and_not_throw(self):
        get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")


    def test_get_request_using_correct_proxy(self):
        prx = proxy("1.20.102.58", 58461)
        response = get_http_request_using_proxy("http://python-lab.ru/documentation/27/stdlib/unittest.html", prx)
        self.assertNotEqual(None, response)

    def test_get_requset_using_wrong_proxy(self):
        prx = proxy("000.000.000.000", 3128)
        response = get_http_request_using_proxy("http://python-lab.ru/documentation/27/stdlib/unittest.html", prx)
        self.assertEqual(None, response)
    
    def test_downloadFile(self):
        file_url = "https://www.google.com.ua/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
        file_name = "tmpFile"
        directory = "tmp"
        filePath = os.path.join(directory, file_name)
        file_size = 5969
        if os.path.isdir(directory) is False:
            os.mkdir(directory)
        
        download_file(file_url, filePath)
        self.assertEqual(True, os.path.isfile(filePath))
        self.assertEqual(file_size,os.path.getsize(filePath))
        os.remove("tmp/tmpFile")

    def test_downloadingFileUsingProxy(self):
        prx = proxy("1.20.102.58", 58461)
        file_url = "https://www.google.com.ua/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
        file_name = "tmpFile"
        directory = "tmp"
        filePath = os.path.join(directory, file_name)
        file_size = 5969
        if os.path.isdir(directory) is False:
            os.mkdir(directory)
        
        download_file(file_url, filePath, prx)
        self.assertEqual(True, os.path.isfile(filePath))
        self.assertEqual(file_size,os.path.getsize(filePath))
        os.remove("tmp/tmpFile")

if __name__ == '__main__':
    unittest.main()