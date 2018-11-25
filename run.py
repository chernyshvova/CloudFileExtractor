from Requester import connector




conx = connector()

conx.get_http_request("https://www.google.com.ua/")
conx.download_file("https://www.google.com.ua/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                    "anme")