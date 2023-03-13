import asyncio
import os

import re
import time

import aiofiles

import aiohttp

import requests


os.chdir('D:\Desktop\kkdongman')

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}





def getm3u8():
    url='https://cj.lziapi.com/index.php/vod/detail/id/48245.html'
    result=requests.get(url,headers)
    list=re.findall(r'<input name="copy_lzm3u8\[]" type="checkbox" value="(.*?)" checked>&nbsp;&nbsp;',result.text)
    title=re.findall(r'片名：(.*?)</p>',result.text,re.S)

    return list,title





def geturls(url):

    index = requests.get(url=url, headers=headers)
    data=re.findall(r'1080x608(.*?).m3u8',index.text,re.S)[0].strip()
    url_2=url.strip('index.m3u8')
    url=url_2+data+'.m3u8'
    resp=requests.get(url=url, headers=headers)

    # print(resp.text)

    obj = re.compile(r',(.*?)#', re.S)

    list = obj.findall(resp.text)

    for i in range(len(list)):
        list[i] = url_2 + data.rsplit('/',1)[0] +'/'+list[i].strip()
    return list

async def download(url,session,n):
    async with session.get(url) as resp :
        async with aiofiles.open(f'{n}.ts','wb') as file:
            await file.write(await resp.content.read())
    print(n)
async def main(list) :
      tasks=[]
      async with aiohttp.ClientSession() as session:

          for i in list :
              tasks.append(asyncio.create_task(download(i,session,list.index(i))))
          await asyncio.wait(tasks)


def merge(list,character,title):
    with open(f'D:\Desktop\movie\{title}{character}.ts',"ab")as f:
        for i in range(len(list)):
            with open(f'{i}.ts','rb') as read:
                f.write(read.read())
            print(f"{i}已被加入")




if __name__ == '__main__':
    # list=geturls()
    # print(list)
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(main(geturls()))
    # merge(list)
    getm3u8=getm3u8()
    title=getm3u8[1][0]
    for i in getm3u8[0] :
        print(getm3u8[0].index(i))
        if(getm3u8[0].index(i)>-1):
            character=i.split('$')[0]
            url=i.split('$')[1]
            list=geturls(url)
            # print(list)
            loop=asyncio.get_event_loop()
            loop.run_until_complete(main(list))
            print('ts下载完毕')
            merge(list,character,title)
            print(f'{character}完成')
            time.sleep(3)
        else:
            continue
    print('全部下载完毕')




