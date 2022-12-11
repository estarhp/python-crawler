import re
import time

import requests

import json

from selenium.webdriver import Chrome

from pprint import pprint


headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'referer': 'https://www.ixigua.com/'
}


url_1='https://v9-xg-web-pc.ixigua.com/463f829f070989a8b048ed63e73ca5ed/63786020/video/tos/cn/tos-cn-o-0004/f94449ad5c3846e8898772fd2f36fd26/media-audio-und-mp4a/?a=1768&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=0&bt=0&cs=0&mime_type=video_mp4&qs=0&rc=QGlqOzR5ZTpmOG9mMzM0NzMzQGEjbDI0YnI0X15kYC0tZC0vc3M%3D&l=2022111911361201021214416801828F4A&btag=38000'
url_2='https://v9-xg-web-pc.ixigua.com/0c692d112c17491359986c20538e6263/63786020/video/tos/cn/tos-cn-o-0004/f94449ad5c3846e8898772fd2f36fd26/media-video-avc1/?a=1768&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1314&bt=1314&cs=0&ds=3&mime_type=video_mp4&qs=0&rc=OGg1aWlmNmY1NmU8PDg3OUBpajs0eWU6ZjhvZjMzNDczM0BhMy9iLzZhNi8xXi9fYGA0YSNsMjRicjRfXmRgLS1kLS9zcw%3D%3D&l=2022111911361201021214416801828F4A&btag=38000'

resp_1=requests.get(url_1,headers)
resp_2=requests.get(url_2,headers)

with open('xigua.mp3','wb') as f:
    f.write(resp_1.content)
with open('xigua.mp4', 'wb') as f:
    f.write(resp_2.content)




# resp=requests.get(url,headers)
#
# print(resp.text)
#
# dict=re.findall(r'window._globalConfig=(.*?)</script>',resp,re.S)[0]
#
# dict=json.loads(dict)
#
# pprint(dict)


# web=Chrome()
#
# web.get('https://www.ixigua.com/6973862328127193636?logTag=e22ad6ca1237823bc449')
# time.sleep(1)
#
# resp=web.page_source
#
# dict=re.findall(r'window._SSR_HYDRATED_DATA=(.*?)<script>',resp,re.S)[0].replace('null','').strip('</script>')

#


