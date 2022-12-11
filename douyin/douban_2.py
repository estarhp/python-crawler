import requests
import re
import csv
for i in range(0,251,25):
    data={
      'start':'t',
      'filter':''
}
    url='https://movie.douban.com/top250'
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
}
    resp=requests.get(url=url,headers=headers,params=data)
    obj=re.compile(r'<span class="title">(?P<name>.*?)</span>.*?'
               r'<br>(?P<year>.*?)&nbsp;/&nbsp;.*?'
               r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                ,re.S)
    page_content=obj.finditer(resp.text)
    with open('data.csv','a',newline='') as f :
         csvwrite=csv.writer(f)
         for i in page_content:
             dict=i.groupdict()
             dict['year']=i.group('year').strip()
             csvwrite.writerow(dict.values())
    resp.close()
