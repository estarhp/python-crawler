import requests
import aiofiles
import re
import aiohttp
import asyncio
import os
os.chdir('D:\Desktop\kkdongman')
async def getvideo(url,n,session):
        async with session.get(url) as resp:
            async with aiofiles.open(f"{n}.ts",'wb') as file:
                await file.write(await resp.content.read())
        print(n)

async def main(list):
    tasks=[]
    n=len(list)
    async with aiohttp.ClientSession() as session:
        for i in range(0,600):
            url="https:"+list[i]+".png"

            tasks.append(asyncio.create_task(getvideo(url,i,session)))
        await asyncio.wait(tasks)

async def main_2(list):
    tasks=[]
    n=len(list)
    async with aiohttp.ClientSession() as session:
        for i in range(600,n):
            url="https:"+list[i]+".png"

            tasks.append(asyncio.create_task(getvideo(url,i,session)))
        await asyncio.wait(tasks)

def getm3u8(url):
    resp = requests.get(url)
    obj = re.compile(r'https:(.*?).png', re.S)
    list = obj.findall(resp.text)
    resp.close()
    return list




def merge(m,n,times):
    lst=[]
    for i in range(m,n):
        lst.append(f"D:\Desktop\kkdongman\{i}.ts")
    s="+".join(lst)
    os.system(f'copy /b {s} D:\Desktop\movie\movie{times}.mp4')




if __name__ == '__main__':
        url='https://yun.ssdm.cc/SBDM/JujutsuKaisen0.m3u8?dpvt=92617999994611210910010412146119119119'

        loop=asyncio.get_event_loop()
        loop.run_until_complete(main(getm3u8(url)))
        loop=asyncio.get_event_loop()
        loop.run_until_complete(main_2(getm3u8(url)))
        merge(0,200,1)
        merge(200,400,2)
        merge(600,800,3)
        merge(800,1000,4)
        merge(1000,1200,5)
        merge(1200,1220,6)