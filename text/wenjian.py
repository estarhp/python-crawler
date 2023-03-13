import requests

import re

cookies = {
    'Hm_lvt_019f21bb3c218020320dc15f8310939a': '1673701472',
    'Hm_lpvt_019f21bb3c218020320dc15f8310939a': '1673701577',
}

headers = {
    'authority': 'www.dongliuxiaoshuo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_019f21bb3c218020320dc15f8310939a=1673701472; Hm_lpvt_019f21bb3c218020320dc15f8310939a=1673701577',
    'pragma': 'no-cache',
    'referer': 'https://www.dongliuxiaoshuo.com/read/AANRAwZT/77907488.html',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

response = requests.get('https://www.dongliuxiaoshuo.com/read/AANRAwZT/77907488_2.html', cookies=cookies, headers=headers)

obj= re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(?P<content>.*?)<br /><br />',re.S)
ret= obj.finditer(response.text)

for i in ret:
  #print(i.group('content'))
  with open('湘西赶尸.txt',mode='a',encoding='utf-8') as f:
    f.writelines(i.group('content')+"\n")
print('over')



