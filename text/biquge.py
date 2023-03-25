import asyncio
import aiohttp
from lxml import etree
import requests
import re
import aiofiles
import os
os.chdir(r'D:\Desktop\杂物\xiaoshuo')
headers={
            "cookie": "Hm_lvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1662623320,1664695116; __gads=ID=21df846c2ab9d266-2275a43ad4d600e1:T=1664695135:RT=1664695135:S=ALNI_MZ7bMnno4jt50DsItHA6Gb7b1-kCQ; __gpi=UID=00000a17127cdaf7:T=1664695135:RT=1664695135:S=ALNI_MbCDkGfFoOlNpEOzdMSaf-Qnnzrng; clickbids=1414; jieqiVisitId=article_articleviews%3D1414; Hm_lpvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1664701911",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
}
url = "https://www.bbiquge.net/book/1416/"
def getpage():
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    list=tree.xpath("/html/body/div[4]/div/select/option/@value")
    return list
def geturls():
    urls = []
    for i in getpage():
        url = f"https://www.bbiquge.net{i}"
        resp=requests.get(url,headers)
        tree=etree.HTML(resp.text)
        list=tree.xpath("/html/body/div[4]/dl/dd/a/@href")
        urls+=list
    return urls
async def download(i):
    async with aiohttp.ClientSession() as f:
        async with f.get(url+i) as resp:
            t=await resp.text()
            list = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />',t)
            text = ",".join(list)
            async with aiofiles.open(i.strip('.html'),"w") as f:
                await f.write(text)
async def main():
    tasks=[]
    for i in geturls():
        tasks.append(asyncio.create_task(download(i)))
    await asyncio.wait(tasks)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

