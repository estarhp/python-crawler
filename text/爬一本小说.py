import json

import requests
import asyncio
import aiohttp
#1.同步操作，拿到所有的cid,title
#2.异步操作，下载所有章节内容
#https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4355370985"}
#https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4355370985","cid":"4355370985|1566855961","need_bookinfo":1}
async def aiodownload(b_id,cid,title):
   data={
       "book_id":b_id,
       "cid":f"{b_id}|{cid}",
       "need_bookinfo":1
   }
   headers={'Cookie': 'BIDUPSID=F7B9A092300182374EB4919FA09412B2; PSTM=1660716803; BAIDUID=1D9F432AA4E6CB1E8B3A57B5E15B4F52:FG=1; Hm_lvt_bf1e478a71b02a743ab42bcfed9d1ff1=1673610424; H_PS_PSSID=36549_37647_38022_36920_38034_37990_37929_26350_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; BAIDUID_BFESS=1D9F432AA4E6CB1E8B3A57B5E15B4F52:FG=1; __bid_n=185aaf58e33cda6f284207; FPTOKEN=o+qPsjRAayofNVNgUaaakLMq3ZfJAZOJBeIYwwJh4wXQkoxJkQrsxx5T+WuLI5Vd5tpkGHlR78anItl6Yl8nftxYJ8Br1E1L2/z3yh26fh8Z6EcfM7ZIovtx7yHTX/2Ypb78ntsjpaGoTkSZ8/op/vHWEQ2f8Jxwyl2HP8s/+9N5FV6IcCueKQG1phKXfeI2IRWnpmZ1Sol4uG7sSJx+q1/SPQYKELoe2H4+O2WblTWi0KzZSVMgKlEgoZC2KiCLMcndef73ztRKMlaR2dJ6Isxbtc5aFvWaZtxb/RHNgL0M/qA5jv7DXFrKrclzwsUFeoOaOKGaYS5fygNQJnKBORa7dtS8DutZC9xr7sg6+sftoGuiWDoJxlsL8fZGyWzXFLjOj9u7uZTkII4M3ZfAgg==',
            'Referer': f'https://dushu.baidu.com/pc/reader?gid=4355370985&cid={cid}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
   data=json.dumps(data)
   url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
   # data=json.dumps(data)
   async with aiohttp.ClientSession() as session:
       async with session.get(url,data=data,headers=headers) as resp:
           print(url)
           dic=await resp.json()


           with open('novel/'+title,mode='w',encoding='utf-8') as f:


             f.write(dic["data"]["novel"]["content"])
             print(dic["data"]["novel"]["content"])




async def getCatalog(url):
    headers={'Cookie': 'BIDUPSID=F7B9A092300182374EB4919FA09412B2; PSTM=1660716803; BAIDUID=1D9F432AA4E6CB1E8B3A57B5E15B4F52:FG=1; Hm_lvt_bf1e478a71b02a743ab42bcfed9d1ff1=1673610424; H_PS_PSSID=36549_37647_38022_36920_38034_37990_37929_26350_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; BAIDUID_BFESS=1D9F432AA4E6CB1E8B3A57B5E15B4F52:FG=1; __bid_n=185aaf58e33cda6f284207; FPTOKEN=o+qPsjRAayofNVNgUaaakLMq3ZfJAZOJBeIYwwJh4wXQkoxJkQrsxx5T+WuLI5Vd5tpkGHlR78anItl6Yl8nftxYJ8Br1E1L2/z3yh26fh8Z6EcfM7ZIovtx7yHTX/2Ypb78ntsjpaGoTkSZ8/op/vHWEQ2f8Jxwyl2HP8s/+9N5FV6IcCueKQG1phKXfeI2IRWnpmZ1Sol4uG7sSJx+q1/SPQYKELoe2H4+O2WblTWi0KzZSVMgKlEgoZC2KiCLMcndef73ztRKMlaR2dJ6Isxbtc5aFvWaZtxb/RHNgL0M/qA5jv7DXFrKrclzwsUFeoOaOKGaYS5fygNQJnKBORa7dtS8DutZC9xr7sg6+sftoGuiWDoJxlsL8fZGyWzXFLjOj9u7uZTkII4M3ZfAgg==|Yy1gYRF77qEWpuC4yXU12fhzTNIGHRa+Aq9FZfwhyl0=|10|e742a32b2b93352862d543b6f9fdc036; Hm_lpvt_bf1e478a71b02a743ab42bcfed9d1ff1=1673610542',
             'Referer': 'https://dushu.baidu.com/pc/reader?gid=4355370985&cid=1566855961',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
    resp=requests.get(url,headers=headers)
    #print(resp.text)
    dic=resp.json()
    tasks=[]
    for item in dic["data"]["novel"]["items"]:
        title=item["title"]
        cid=item["cid"]
        #print(title)
        #print(cid)
        tasks.append(asyncio.create_task(aiodownload(b_id,cid,title)))
    await asyncio.wait(tasks)

if __name__=='__main__':
    b_id="4355370985"
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(url))