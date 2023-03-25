import requests

cookies = {
    'fid': '1842',
    'lv': '2',
    '_uid': '239076715',
    'UID': '239076715',
    'vc': '4B8AF6C48FF457EF9A77C9B3DF081AC6',
    'xxtenc': '97e87e1f56dda849187e691019fb07d8',
    'uf': 'b2d2c93beefa90dc7d0f9867706e3a6efc0dcf14862ad0cf99ffbd15bf9817c675d02521c584b2346d95c9b110c0b9da913b662843f1f4ad6d92e371d7fdf644d490c7da6f959ca6fd68be96b6183b1a9f5a410d7b2927a251762f27a80caf53b0df437cc03bd2a2',
    '_d': '1669188837303',
    'vc2': '0C91E9AD13C0CDA64BBC53580D160EA4',
    'vc3': 'M3kzffVmJ2y2ny%2FrAI4fNOWpPzyGaDVHxrny3S%2BIco%2Bj55YeCUmZZ23l7NUH2AQl3RzN%2FF7Orq8XUVj9k1a5%2BuZaJGXL1U3SMwL473fhJ0Jw4w7Z%2BM1KVUGi55s8kVxmBM3Lh%2BLZMHeBwMc7rKc7F3TmMclIiK2YNmLzGWGLASU%3Db8d742f4868eabfc24481aa674fc5d10',
    'DSSTASH_LOG': 'C_38-UN_100-US_239076715-T_1669188837305',
    'source': '""',
    'spaceFid': '1842',
    'spaceRoleId': '""',
    'JSESSIONID': 'B1197319FC6B2413E09A30D74F4717B1',
    'route': '0dabf1ff125db663fbab68e20f62bc85',
    'thirdRegist': '0',
    '_industry': '5',
    '226696898cpi': '275935756',
    '226696898ut': 's',
    '226696898t': '1669624634449',
    '226696898enc': '41a3541b7113ce95e007d7a9fabcacd6',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'fid=1842; lv=2; _uid=239076715; UID=239076715; vc=4B8AF6C48FF457EF9A77C9B3DF081AC6; xxtenc=97e87e1f56dda849187e691019fb07d8; uf=b2d2c93beefa90dc7d0f9867706e3a6efc0dcf14862ad0cf99ffbd15bf9817c675d02521c584b2346d95c9b110c0b9da913b662843f1f4ad6d92e371d7fdf644d490c7da6f959ca6fd68be96b6183b1a9f5a410d7b2927a251762f27a80caf53b0df437cc03bd2a2; _d=1669188837303; vc2=0C91E9AD13C0CDA64BBC53580D160EA4; vc3=M3kzffVmJ2y2ny%2FrAI4fNOWpPzyGaDVHxrny3S%2BIco%2Bj55YeCUmZZ23l7NUH2AQl3RzN%2FF7Orq8XUVj9k1a5%2BuZaJGXL1U3SMwL473fhJ0Jw4w7Z%2BM1KVUGi55s8kVxmBM3Lh%2BLZMHeBwMc7rKc7F3TmMclIiK2YNmLzGWGLASU%3Db8d742f4868eabfc24481aa674fc5d10; DSSTASH_LOG=C_38-UN_100-US_239076715-T_1669188837305; source=""; spaceFid=1842; spaceRoleId=""; JSESSIONID=B1197319FC6B2413E09A30D74F4717B1; route=0dabf1ff125db663fbab68e20f62bc85; thirdRegist=0; _industry=5; 226696898cpi=275935756; 226696898ut=s; 226696898t=1669624634449; 226696898enc=41a3541b7113ce95e007d7a9fabcacd6',
    'Referer': 'https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=644807541&courseId=228023735&clazzid=62910554&cpi=265808211&enc=6a0a64b16b89b60c4142df57a66af12f&mooc2=1&openc=a4269d84fa9fbb24628d6f44c778b140',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://detect.chaoxing.com/api/monitor?version=1669628128975&refer=http://i.mooc.chaoxing.com&from=&jsoncallback=jsonp004370921984462295&t=1669628459479', cookies=cookies, headers=headers)
print(response.text)