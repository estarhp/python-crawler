import json

import re

import requests

import subprocess

from pprint import pprint

import os

os.chdir(r'D:\Desktop\bilibili\un_merge')

def geturls(url):
    resp=requests.get(url=url,headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    })
    # print(resp.text)
    name=re.findall(r'<title .*?>(.*?)”</title>',resp.text,re.S)[0]

    dict=re.findall(r'<script>window.__playinfo__=(.*?)</script>',resp.text,re.S)
    dict=json.loads(dict[0])
    # pprint(dict)
    mp3_url=dict['data']['dash']['audio'][0]['baseUrl']
    mp4_url=dict['data']['dash']['video'][0]['base_url']
    return mp4_url,mp3_url,name


def downmp4(url,name):
    headers={
        'if-range': 'Sun, 13 Nov 2022 03:43:41 GMT',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'referer': 'https://www.bilibili.com/video/BV1hv4y1S7d3/?vd_source=ffeb0ac17cb484d79e30da53310698e9'
    }
    resp=requests.get(url=url,headers=headers)
    with open(f'{name}.mp4','wb') as file:
        file.write(resp.content)
        print('ok1')

def downmp3(url,name):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'referer': 'https://www.bilibili.com/video/BV1hv4y1S7d3/?vd_source=ffeb0ac17cb484d79e30da53310698e9',
        'if-range': 'Sat, 12 Nov 2022 17:34:51 GMT'
    }
    resp=requests.get(url=url,headers=headers)
    with open(f'{name}.mp3','wb') as file:
        file.write(resp.content)
        print('ok2')

def merge_data(name):
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    COMMAND = f'ffmpeg -i D:/Desktop/bilibili/un_merge/video.mp4 -i D:/Desktop/bilibili/un_merge/audio.mp3 -c:v copy -c:a aac -strict experimental D:/Desktop/bilibili/merged/{name}.mkv'
    subprocess.run(COMMAND, shell=True)






if __name__ == '__main__':
    url='https://www.bilibili.com/bangumi/play/ss41417?from_spmid=666.4.0.0'
    datas=geturls(url)
    downmp4(datas[0],datas[2])
    downmp3(datas[1],datas[2])
    merge_data(datas[2])