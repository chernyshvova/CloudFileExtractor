import unittest
from proxy import proxy

class HTTPToolsTests(unittest.TestCase):
    def test_proxy_creating(self):
        prx = proxy("host", 123)
        self.assertEqual("host", prx.host)
        self.assertEqual(123, prx.port)
    
    def test_proxy_to_str(self):
        prx = proxy("host", 123)
        self.assertEqual("host:123", prx.to_str())