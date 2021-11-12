
__athor__ = 'Shobhit'

import requests, random, json, threading


def test_ip(ip: int, port: int):
    ip_http = {
        "http": "http://",
    }
    ip_https = {
        "https": "https://"
    }
    proxies.keys()[0] ="http://"+ip ":" + port
    request = requests.get(url="https://ipinfo.io/json", timeout=100000)


proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080",
}


request = requests.get(url="https://ipinfo.io/json", timeout=100000, proxies=proxies)
print(request.text)
