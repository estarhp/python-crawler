import requests
import re
import os
import asyncio
import aiohttp
import aiofiles
from lxml import etree
os.chdir(r'D:\Desktop\kkdongman')
headers={
    "Cookie": "Hm_lvt_5262cff1b6644c49657918e2eb87ea4c=1665036280; Hm_lpvt_5262cff1b6644c49657918e2eb87ea4c=1665036280",
    "Referer": "https://cn.bing.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"
}
url='https://www.kakadm.cc/play/2597-0-1.html'

def getpage(url):
    resp = requests.get(url, headers)
    tree=etree.HTML(resp.text)
    list=tree.xpath("/html/body/div[4]/div/div/div/table/tbody/tr[3]/td[1]/iframe[2]/@src")
    return list[0]

def geturl(url):
    resp=requests.get(url,headers)
    obj = re.compile(r'https:(.*?).ts', re.S)
    list = obj.findall(resp.text)
    return list

async def download(url,n):
    async with aiohttp.ClientSession() as  f:
        async with f.get(url,headers=headers) as resp:
             async with aiofiles.open(f'{n}.mp4',"wb") as w:
                await w.write(await resp.content.read())

async def func(list):
    tasks=[]
    for i in list:
        n = list.index(i)
        i = 'https:' + i + '.ts'
        tasks.append(asyncio.create_task(download(i,n)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(func(geturl(getpage(url))))

