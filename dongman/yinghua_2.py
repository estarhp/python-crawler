import time

import requests

import aiofiles

import re

import aiohttp

import asyncio

import os

os.chdir('D:\Desktop\kkdongman')

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

async def getvideo(url, n, session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"{n}.ts", 'wb') as file:
            await file.write(await resp.content.read())
    print(n)


async def main(list):
    tasks = []
    n = len(list)
    async with aiohttp.ClientSession() as session:
        for i in range(0,n):
            url = "https:" + list[i] + ".png"

            tasks.append(asyncio.create_task(getvideo(url, i, session)))
        await asyncio.wait(tasks)


def getm3u8(url):
    resp = requests.get(url,headers)
    obj = re.compile(r'https:(.*?).png', re.S)
    list = obj.findall(resp.text)
    resp.close()
    return list


def merge(url,n):
    lst = []
    for i in range(len(getm3u8(url))):
        lst.append(f"D:\Desktop\kkdongman\{i}.ts")
    s = "+".join(lst)
    name=f'SummerTimeRendering{n}'
    os.system(f'copy /b {s} D:\Desktop\movie\{name}.mp4')


if __name__ == '__main__':
    dpvt = 92656899994611210910010412146119119119
    for n in range(8,26):
        if n<10:
            url = f'https://yun.ssdm.cc/SBDM/SummerTimeRendering0{n}.m3u8?dpvt={dpvt}'

            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(getm3u8(url)))
            merge(url,n)
            time.sleep(5)
        else:
            url = f'https://yun.ssdm.cc/SBDM/SummerTimeRendering{n}.m3u8?dpvt={dpvt}'

            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(getm3u8(url)))
            merge(url,n)
            time.sleep(5)
