import requests


proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
request = requests.get(url="https://ipinfo.io/json", timeout=100000, proxies=proxies)
print(request.text)

ip = {}


for pa in range(1, 70):
    ip.append(emp["data"][pa]["ip"] + ":" + emp["data"][pa]["port"])

print(ip)
