import re
import requests
url='https://www.dygod.net/'
headers={
    'cookie': 'Hm_lvt_f7abbae08c28b34b707daf8674110ce5=1661010731,1661570950,1661581329,1662451247; Hm_lpvt_f7abbae08c28b34b707daf8674110ce5=1662451247',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
}
resp=requests.get(url,headers)
resp.encoding='gb2312'
obj=re.compile(r'title=".*?">(?P<name>.*?)</a><span><font',re.S)
obj_2=re.compile(r'<li><a href=\'(.*?)\' title=".*?">.*?</a><span><font color=#FF0000>09-06</font></span></li>',re.S)
obj_3=re.compile(r'/(.*?)/')
t=obj_2.findall(resp.text)
a=[]
for q in t:
    p=obj_3.findall(q)
    if 'hytv' in p:
        a.append(q)
u=[]
for i in a:
    url_2=url+i.strip('/')
    u.append(url_2)
url_3=u[0]
headers_2={
    'cookie': 'Hm_lvt_f7abbae08c28b34b707daf8674110ce5=1661010731,1661570950,1661581329,1662451247; Hm_lpvt_f7abbae08c28b34b707daf8674110ce5=1662515988',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
}
resp_2=requests.get(url=url_3,headers=headers_2)
resp_2.encoding='gb2312'
obj_4=re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>',re.S)
result=obj_4.findall(resp_2.text)
with open('下载地址.txt', 'a') as f:
     for i in result:
         f.write(i)
         f.flush()
         f.write('\n')
resp.close()
resp_2.close()