

#https://awmproxy.com/freeproxy.php
class proxy:
    host = ""
    port = ""

    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def to_str(self):
        return self.host + ":" + str(self.port)