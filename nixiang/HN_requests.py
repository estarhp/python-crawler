import requests
import execjs
cookies = {
    'SESSION': 'MTZjMjk0ZTMtZjE2MC00MGIzLWE2YTktNDE0NDUwNjU5NTk2',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'SESSION=MTZjMjk0ZTMtZjE2MC00MGIzLWE2YTktNDE0NDUwNjU5NTk2',
    'Origin': 'https://login.hnzwfw.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://login.hnzwfw.gov.cn/tacs-uc/login/index?refer=na',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'EMU3uuB8ldNLTTtwwuvh2O++zjDpSPsKi3sCBVDwW13XPz37zPXoRBSV4zOf8swo+ztMBCf5qlWqg6BgZwrR7DvNoGcfKI50jtbn/rIRbFJ5STNU9Eaq+/uQYlktfEH0bMX3bEW+vxuhykpu1PnynTU6ARk+nh7u0K9xklhPmhTR7hwpPYs8gDsOkRF7QzhkbmOsYi7QM4cLUdK+H/Rvl5atSj2zeaNW8mVytpCd9xDF325gs9PWY+BcZdxF/Ct4DofVHiC2TkXYg5dnsYe5hcv/xlZmPNBXi2U76eLr1ZEtMzNyEcPFkCPVGTYDinAjs6A0d1iUbM5tVZFJt6uhkQ==',
}

data = {
    'backUrl': '',
    'loginNo': 'dYicz6QIy3H6zneLfDFNV/o4sHEyvM/5ehvTSOuY6qtw+kpcbBE/HZlNoFtrkgi/JjQLRxcX4jt1LvrGMRDAQ4jze0C0VZgZYZJPsNbwqhkW0j9VMlw0Q6Rxh9InxzPWE4vqCLWFpB9PyoDRZlcbKLj/yD3x+tckLIPPJr0X9e+XlAzidM6SWMCMsNavFPQ/v05IMUJCHxKXpcEZJTglgZ72ZPlgn22Um/Deiigu6coc+yOqEZ/YhZeu1gRQqBC/DMF6+7mr8aIHghn54MOYonywdJXii5AOgu2zczLvub5FoL7WJA94IJPoO49shKBwFRroD2bddBassZEpR67GSg==',
    'loginPwd': 'reYCAilSEws2Q0MBdhuySGucvL2kG44BvPqvbZynsECXFjj6NWbUvz24Swd2A1gVlL91Y35i3Wn7cNJlnJg/AMyE22B664eN5Byp2zqzRG4rKgIAKG3SB9JBhDzqBfbZbBnAR+qnVvotZGyYAT2wyX7iLCSWGVTi1r9NJY+PnbeDFiFKV3ITb/k0JdCzkONm22k+kp3sgdIc8jsu7OCyBaNCzPGjqsfBLusqJTDUtgCcD9GPQcRHw7sB88Pl3peQWsd6CVZpmNIH7/Rhra5T908+KKzgWjZkkcuxWpYN6/2i5vzU5gRqyM0sM9YFGN2hm3zWGYYUJTrF1gQoI4J7YQ==',
    'code': 'e5c0aad2-6528-4d7c-9ad1-d944ee92f07d',
    'requestUUID': '0e34793f-9001-4677-a36c-adbd79251e30',
    'guoBanAuthCode': '',
}

UUID = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/uploadIdentifier', cookies=cookies, headers=headers)
data['requestUUID']=UUID.json()["data"]
logincode = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/login/verCode', cookies=cookies, headers=headers)
data["code"]=logincode.json()["data"]


personname="13990205914"
password="thyqwert12345"

data['loginNo']=execjs.compile(open("HN.js","r").read()).call("rsa_encrypt",personname)
data['loginPwd']=execjs.compile(open("HN.js","r").read()).call("rsa_encrypt",password)

response = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/loginNo', cookies=cookies, headers=headers, data=data)


print(response.text)