import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5



import requests

cookies = {
    '_zw_kvani5r': '2d747b63f5ce84497d9ddde238db66fe4cfe9685aa41e951f7ef7a9e5b12ae68f49c20a3',
    'sendflag': '20221214194853243986',
    'lgToken': 'mhrz92de576c41b39bfd75e358a14580',
    'CaptchaCode': 'rXRrVF',
}

def encrypt_str(data) :
    key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgDq4OqxuEisnk2F0EJFmw4xKa5IrcqEYHvqxPs2CHEg2kolhfWA2SjNuGAHxyDDE5MLtOvzuXjBx/5YJtc9zj2xR/0moesS+Vi/xtG1tkVaTCba+TV+Y5C61iyr3FGqr+KOD4/XECu0Xky1W9ZmmaFADmZi7+6gO9wjgVpU9aLcBcw/loHOeJrCqjp7pA98hRJRY+MML8MK15mnC4ebooOva+mJlstW6t/1lghR8WNV8cocxgcHHuXBxgns2MlACQbSdJ8c6Z3RQeRZBzyjfey6JCCfbEKouVrWIUuPphBL3OANfgp0B+QG31bapvePTfXU48TYK0M5kE+8LgbbWQIDAQAB"
    rsakey=RSA.importKey(base64.b64decode(key))
    cipher=PKCS1_v1_5.new(rsakey)
    cipher_text=base64.b64encode(cipher.encrypt(data.encode(encoding="utf-8")))
    return cipher_text.decode()

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_zw_kvani5r=2d747b63f5ce84497d9ddde238db66fe4cfe9685aa41e951f7ef7a9e5b12ae68f49c20a3; sendflag=20221214194853243986; lgToken=mhrz92de576c41b39bfd75e358a14580; CaptchaCode=rXRrVF',
    'Origin': 'https://login.10086.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://login.10086.cn/html/login/login.html?channelID=10000&backUrl=https://login.10086.cn/html/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'accountType': '02',
    'account':  encrypt_str("13990205914@139.com"),
    'password': encrypt_str("thyqwert"),
    'pwdType': '03',
    'inputCode': 'naaxnx',
    'backUrl': 'https://login.10086.cn/html/login',
    'rememberMe': '1',
    'channelID': '10000',
    'loginMode': '01',
    'protocol': 'https:',
    'timestamp': '1671025073634',
}

response = requests.post('https://login.10086.cn/login.htm', cookies=cookies, headers=headers, data=data)


print(response.text)