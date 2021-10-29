import requests

proxya = {"https": "https://80.82.60.62:8080"}

request = requests.get(url="https://ipinfo.io/json", timeout=10000)
print(request.text)
