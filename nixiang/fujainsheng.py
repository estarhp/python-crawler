import time

import requests

import execjs


url='https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo'

json_data={

    "pageNo": 1,
    "pageSize": 20,
    "total": 0,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2022-05-25 00:00:00",
    "EndTime": "2022-11-25 23:59:59",
    "createTime": [],
    "ts": round(time.time()*1000)
}

portal_sign=execjs.compile(open('request.js','r',encoding='utf-8').read()).call('d',json_data)

print(portal_sign)
headers={
    'Accept': "application/json, text/plain, */*",
    'portal-sign': portal_sign,
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.56'
}

resp=requests.post(url=url,json=json_data,headers=headers)

print(resp.json()['Data'])


data=execjs.compile(open('data.js','r',encoding='utf-8').read()).call('b',resp.json()["Data"])


print(data)



