import requests

import execjs
url='http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008'

mcode=execjs.compile(open('mecode.js','r').read()).call('indexcode.getResCode')

print(mcode)
headers={
    'Referer': 'http://webapi.cninfo.com.cn/',



    "mcode": mcode,

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

params={
    "scode": "000001-SZE",
    "sdate": "2021-11-26",
    "edate": "2022-11-26",
    "ctype": '0'
}

resp=requests.post(url=url,headers=headers,params=params)
print(resp.json())