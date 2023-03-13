import requests


url="https://xueqiu.com/1107854878/242310856"


resp=requests.get(url,headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
})

print(resp.headers)