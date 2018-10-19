from connector.HTTPTools import *
import unittest

class HTTPToolsTests(unittest.TestCase):
    def test_correct_queryWithoutExceptions(self):
        get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")

    def test_correct_response(self):
        response = get_http_request("http://python-lab.ru/documentation/27/stdlib/unittest.html")
        self.assertEqual(200, response.getcode())

    def test_wrong_url(self):
        response = get_http_request("dasdadasdsadas")
        self.assertEqual(None, response)

if __name__ == '__main__':
    unittest.main()