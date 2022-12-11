import requests

resp=requests.get('https://www.baidu.com/')

print(resp.text)
