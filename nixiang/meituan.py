import json
import time

import requests

import b64

import  zlib


cookies = {
    '_lxsdk_cuid': '184b8f39c6ec8-00ffa9c60bf9a-26021e51-e1000-184b8f39c6ec8',
    'lat': '29.533545',
    'lng': '106.605629',
    '_lx_utm': 'utm_source%3Dgoogle%26utm_medium%3Dorganic',
    'ci3': '45',
    'IJSESSIONID': 'node01xikkpoyzu4kf3l432k2wzl420156461',
    'iuuid': '5909D7B1B2764B58DA21D440E9D0E00794FE82AA7A33027B7D9B276CDC670E79',
    '_lxsdk': '5909D7B1B2764B58DA21D440E9D0E00794FE82AA7A33027B7D9B276CDC670E79',
    'webp': '1',
    'latlng': '29.533545,106.605629,1669550313405',
    '__utma': '74597006.592738584.1669550314.1669550314.1669550314.1',
    '__utmc': '74597006',
    '__utmz': '74597006.1669550314.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '_hc.v': 'a040c97e-1609-81e8-5136-9bbbbd6a074a.1669550382',
    'WEBDFPID': '6710z9zv1u85508x1z12u46u36zyw67v815y1u48xxv979585y8uv4w1-1984910382044-1669550381575EWCUQUWfd79fef3d01d5e9aadc18ccd4d0c95071743',
    'cityname': '%E9%87%8D%E5%BA%86',
    '__utmb': '74597006.13.9.1669550505263',
    'i_extend': 'C_b1Gimthomepagecategory11H__a',
    'meishi_ci': '45',
    'cityid': '45',
    '_yoda_verify_resp': 'Rs52DZneaaG26E7XbGeZ2lyCfZFJBJgzfx7r2UxcZVmZcTJrCLYjR0Gqazt4AJRoEc7f6htn8NoCQHnKkPNpfua%2Bc7iudV%2Fu%2B9x96C%2BpVoS43gwFbPXijDMeiCS8rFixiixwsIDKMQ7C%2F8bpD74ATM22Oo%2FJ8QjST%2FdJyKu1wVRQa8tHpR7YJUoWul9iJthqW70ICFqsTDI7rWg%2BSUdLMSmFcXJrig2fe8XOacZIRHS%2FYnGykNy3KjWCvQOFjjou7%2BdrTD7KEbHFqa8LZvDaT8pje%2FoMvsc31KJKFPjRlxia41N%2FGhKiOddtsPUQdJIgTuGwKLRygnA8TEdV0qAwaOhf%2FeTW0%2FRrZTREIs2irXtEq6ObQEjl8i7PerCxP2Y5',
    '_yoda_verify_rid': '16291a9c7e400030',
    'ci': '1',
    'rvct': '1',
    '__mta': '188587287.1669550615159.1669550615159.1669550615159.1',
    'client-id': '57a6b0e8-ca4f-4fcb-970d-cfe8f6fee188',
    'uuid': 'ce33ac1d119543799f6f.1669550636.1.0.0',
    'mtcdn': 'K',
    'lt': 'AgGZHaNIoW_gsw_nCGXj0Xe58CjAQBRl4mjFmXZkWNId10I_Aru6WH1W54aOHoDXjwk6p4XHAwMfTwAAAAAWFQAALz0sDg4bvKipR6suz4XAPDY6-nsf-66y3nGCtsEkCU00j0PadfAkrVsgB1VoZgiv',
    'u': '3827220469',
    'n': 'jrz837678287',
    'token2': 'AgGZHaNIoW_gsw_nCGXj0Xe58CjAQBRl4mjFmXZkWNId10I_Aru6WH1W54aOHoDXjwk6p4XHAwMfTwAAAAAWFQAALz0sDg4bvKipR6suz4XAPDY6-nsf-66y3nGCtsEkCU00j0PadfAkrVsgB1VoZgiv',
    'unc': 'jrz837678287',
    'firstTime': '1669551303873',
    '_lxsdk_s': '184b8f39c6f-5f5-852-0d7%7C%7C164',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_lxsdk_cuid=184b8f39c6ec8-00ffa9c60bf9a-26021e51-e1000-184b8f39c6ec8; lat=29.533545; lng=106.605629; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; ci3=45; IJSESSIONID=node01xikkpoyzu4kf3l432k2wzl420156461; iuuid=5909D7B1B2764B58DA21D440E9D0E00794FE82AA7A33027B7D9B276CDC670E79; _lxsdk=5909D7B1B2764B58DA21D440E9D0E00794FE82AA7A33027B7D9B276CDC670E79; webp=1; latlng=29.533545,106.605629,1669550313405; __utma=74597006.592738584.1669550314.1669550314.1669550314.1; __utmc=74597006; __utmz=74597006.1669550314.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _hc.v=a040c97e-1609-81e8-5136-9bbbbd6a074a.1669550382; WEBDFPID=6710z9zv1u85508x1z12u46u36zyw67v815y1u48xxv979585y8uv4w1-1984910382044-1669550381575EWCUQUWfd79fef3d01d5e9aadc18ccd4d0c95071743; cityname=%E9%87%8D%E5%BA%86; __utmb=74597006.13.9.1669550505263; i_extend=C_b1Gimthomepagecategory11H__a; meishi_ci=45; cityid=45; _yoda_verify_resp=Rs52DZneaaG26E7XbGeZ2lyCfZFJBJgzfx7r2UxcZVmZcTJrCLYjR0Gqazt4AJRoEc7f6htn8NoCQHnKkPNpfua%2Bc7iudV%2Fu%2B9x96C%2BpVoS43gwFbPXijDMeiCS8rFixiixwsIDKMQ7C%2F8bpD74ATM22Oo%2FJ8QjST%2FdJyKu1wVRQa8tHpR7YJUoWul9iJthqW70ICFqsTDI7rWg%2BSUdLMSmFcXJrig2fe8XOacZIRHS%2FYnGykNy3KjWCvQOFjjou7%2BdrTD7KEbHFqa8LZvDaT8pje%2FoMvsc31KJKFPjRlxia41N%2FGhKiOddtsPUQdJIgTuGwKLRygnA8TEdV0qAwaOhf%2FeTW0%2FRrZTREIs2irXtEq6ObQEjl8i7PerCxP2Y5; _yoda_verify_rid=16291a9c7e400030; ci=1; rvct=1; __mta=188587287.1669550615159.1669550615159.1669550615159.1; client-id=57a6b0e8-ca4f-4fcb-970d-cfe8f6fee188; uuid=ce33ac1d119543799f6f.1669550636.1.0.0; mtcdn=K; lt=AgGZHaNIoW_gsw_nCGXj0Xe58CjAQBRl4mjFmXZkWNId10I_Aru6WH1W54aOHoDXjwk6p4XHAwMfTwAAAAAWFQAALz0sDg4bvKipR6suz4XAPDY6-nsf-66y3nGCtsEkCU00j0PadfAkrVsgB1VoZgiv; u=3827220469; n=jrz837678287; token2=AgGZHaNIoW_gsw_nCGXj0Xe58CjAQBRl4mjFmXZkWNId10I_Aru6WH1W54aOHoDXjwk6p4XHAwMfTwAAAAAWFQAALz0sDg4bvKipR6suz4XAPDY6-nsf-66y3nGCtsEkCU00j0PadfAkrVsgB1VoZgiv; unc=jrz837678287; firstTime=1669551303873; _lxsdk_s=184b8f39c6f-5f5-852-0d7%7C%7C164',
    'Referer': 'https://bj.meituan.com/meishi/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


data="areaId=0&cateId=0&cityName=北京&dinnerCountAttrId=&optimusCode=10&originUrl=https://bj.meituan.com/meishi/&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=3827220469&uuid=ce33ac1d119543799f6f.1669550636.1.0.0"

sign=base64.b64encode(zlib.compress(data.encode())).decode()


iP={
    "rId": 100900,
    "ver": "1.0.6",
    "ts": round(time.time()*1000),
    "cts": round(time.time()*1000)+1000,
    "brVD": [
        150,
        599
    ],
    "brR": [
        [
            1280,
            720
        ],
        [
            1280,
            672
        ],
        24,
        24
    ],
    "bI": [
        "https://bj.meituan.com/meishi/",
        ""
    ],
    "mT": [],
    "kT": [],
    "aT": [],
    "tT": [],
    "aM": "",
    "sign": sign
}

token=base64.b64encode(zlib.compress(str(iP).encode())).decode()



params = {
    'cityName': '北京',
    'cateId': '0',
    'areaId': '0',
    'sort': '',
    'dinnerCountAttrId': '',
    'page': '1',
    'userId': '3827220469',
    'uuid': 'ce33ac1d119543799f6f.1669550636.1.0.0',
    'platform': '1',
    'partner': '126',
    'originUrl': 'https://bj.meituan.com/meishi/',
    'riskLevel': '1',
    'optimusCode': '10',
    '_token':token
}


print(token)


response = requests.get('https://bj.meituan.com/meishi/api/poi/getPoiList', params=params, cookies=cookies, headers=headers)
print(response.text)