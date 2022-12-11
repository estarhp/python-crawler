import re
import requests
import os
import csv
from concurrent.futures import ThreadPoolExecutor
os.chdir(r'D:\Desktop\杂物')
def func(n):
    url=' http://www.xinfadi.com.cn/getPriceData.html'
    resp=requests.post(url,headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    },data={
            'limit': '20',
            'current':n,
            'pubDateStartTime': '',
            'pubDateEndTime': '',
            'prodPcatid': '',
            'prodCatid': '',
            'prodName': ''
    })
    resp.encoding='utf-8'
    list1=re.findall(r'"prodName":"(.*?)",',resp.text,re.S)
    list2=re.findall(r'"prodCat":"(.*?)",',resp.text,re.S)
    list3=re.findall(r'"lowPrice":"(.*?)",',resp.text,re.S)
    list4=re.findall(r'"highPrice":"(.*?)"',resp.text,re.S)
    list5=re.findall(r'"avgPrice":"(.*?)",',resp.text,re.S)
    list6=re.findall(r'"place":"(.*?)",',resp.text,re.S)
    list7=re.findall(r'"unitInfo":"(.*?)",',resp.text,re.S)
    list8=re.findall(r'"pubDate":"(.*?)",',resp.text,re.S)
    print(n)
    for q,w,e,r,t,y,u,i in zip(list1,list2,list3,list4,list5,list6,list7,list8,):
        with open('data.csv','a',newline='') as f:
            csvwrite=csv.writer(f)
            csvwrite.writerow([q,w,e,r,t,y,u,i])
if __name__ == '__main__':
    with ThreadPoolExecutor(200) as t:
        for n in range(1,18054):
            t.submit(func,n)
print('over!!!!')










