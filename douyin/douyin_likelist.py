from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time

from concurrent.futures import ThreadPoolExecutor

import os

import requests

import re

from douyin_img import download

from subprocess import run






os.chdir(r'D:\Desktop\从抖音爬到的视频')

def xiala():
    js = "var q=document.documentElement.scrollTop=10000"
    web.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=10000"
    web.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=10000"
    web.execute_script(js)
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=10000"
    web.execute_script(js)
    time.sleep(2)
def download_2(result,name):
    resp = requests.get(result, headers={
        'cookie': 'douyin.com; ttwid=1%7C4PfqWzjTeZsLO8zyYOzLf7CQby5DcNN4zkSThvcCoVM%7C1660557974%7C9c9794fe7933189cf94bebb246397beaa594887d738b13218b13e820797e5412; strategyABtestKey=1660557976.692; s_v_web_id=verify_l6ulcfbf_5KJ83orR_O3sM_42dH_BvCc_nEnF9RzcHjbc; passport_csrf_token=9072f640080f068c03d59db60d30cc54; passport_csrf_token_default=9072f640080f068c03d59db60d30cc54; ttcid=c425c71e5a5240f496105458282b00da18; n_mh=0Nq0PtRnjxLi1K3bqi9jIyTqihwy5Eelyhf0BFF9bM0; sso_uid_tt=de6fd5b6fe99474b61a875d1e749fc96; sso_uid_tt_ss=de6fd5b6fe99474b61a875d1e749fc96; toutiao_sso_user=57490f73895f175fb1a905390c296ea6; toutiao_sso_user_ss=57490f73895f175fb1a905390c296ea6; sid_ucp_sso_v1=1.0.0-KGNkZDQ3Y2UwM2YwM2MxNzY5YmJlMmQxNDQyYjVjZTgwYzkyMTgxNmUKHQj_uODV3gIQtbXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; ssid_ucp_sso_v1=1.0.0-KGNkZDQ3Y2UwM2YwM2MxNzY5YmJlMmQxNDQyYjVjZTgwYzkyMTgxNmUKHQj_uODV3gIQtbXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; odin_tt=7e4bb327515c33b6f87ade3aad50f19c6323350e395994565f2b55ea40f1039d1c0cf240ef0fef412f803b945978d11e; sid_guard=57490f73895f175fb1a905390c296ea6%7C1660558006%7C5184000%7CFri%2C+14-Oct-2022+10%3A06%3A46+GMT; uid_tt=de6fd5b6fe99474b61a875d1e749fc96; uid_tt_ss=de6fd5b6fe99474b61a875d1e749fc96; sid_tt=57490f73895f175fb1a905390c296ea6; sessionid=57490f73895f175fb1a905390c296ea6; sessionid_ss=57490f73895f175fb1a905390c296ea6; sid_ucp_v1=1.0.0-KGE4YzllNjQ2MmI1M2I0Zjg4MGM1ZTYwYjE2NWFmNTdlMjk1MzZhYjUKHQj_uODV3gIQtrXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; ssid_ucp_v1=1.0.0-KGE4YzllNjQ2MmI1M2I0Zjg4MGM1ZTYwYjE2NWFmNTdlMjk1MzZhYjUKHQj_uODV3gIQtrXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAHiF_1qLSnSkvrBJtTnwyrQEMnKWvypI9JjFDRQ2yOE8%2F1660579200000%2F0%2F1660558009912%2F0%22; _tea_utm_cache_1243=undefined; THEME_STAY_TIME=%22299396%22; IS_HIDE_THEME_CHANGE=%221%22; __ac_nonce=062fa389800a44c2dcf95; __ac_signature=_02B4Z6wo00f01piVOogAAIDAeiBKHgjOemqYpT4AAMTrKiQp1RkAYe6lguL33R6pIM0RqBqs8DtSkMHIxEyD8pdQiFiUYc7lCzXIBjB.b4lnaAnocgazVzkrNnNrY4izenlrnfR9eDX.Hvdv14; MONITOR_WEB_ID=088b39e1-7e30-4218-8d14-2c6625410fa3; douyin.com; msToken=0fJfq4xf6t8mwrit4O29j7K_FGynpJEGidTFm277js9UbkUbN3FA89AT4W1I_crGfwugtkD6G4eNCY9mG9DLAHJFcHlWXrv9lrf9mIw2k6DduN7HknULpA==; home_can_add_dy_2_desktop=%221%22; msToken=rDP9A2hqh5xL-WDQEbNhC3u5ilkEV1JTG37gjLVlwGObEBBBm6wVu-GNqDwfDcwwIe84mvIu8ave11F-WXv28zQ0Q6O-mBR4FIhxBCVkBB3tQDxvMZzSPz_iluIJ15c=; tt_scid=uDo7yqeK6-Qdpy5wCwHnhzi4-EEg2udJ6eMZSpUbZ.dcZKUmgsOx0ocD5wSlc-sq4c77',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
    })
    with open(name+'.mp4','wb') as f:
        f.write(resp.content)
    resp.close()




def getresult(url):
    bro = webdriver.Chrome()
    bro.get(url)
    time.sleep(3)
    bro.find_element("class name", "dy-account-close").click()
    result= bro.find_element('xpath','/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[1]').get_attribute("src")
    name=bro.title
    download_2(result,name)
    print("ok")



if __name__ == '__main__':

    options = Options()
    options.add_experimental_option("debuggerAddress","127.0.0.1:9527")#"debuggerAddress",
    web = webdriver.Chrome(options=options)
    url = 'https://www.douyin.com/user/MS4wLjABAAAAHiF_1qLSnSkvrBJtTnwyrQEMnKWvypI9JjFDRQ2yOE8?showTab=like'
    web.get(url)
    time.sleep(2)
    xiala()
    list_video = re.findall(r'<a href="/video/(.*?)"',web.page_source,re.S)
    list_note=re.findall(r'<a href="/note/(.*?)"',web.page_source,re.S)
    print(list_note,list_video)
    with ThreadPoolExecutor(5) as pool:
        for t in list_note:

            download('https://www.douyin.com/note/'+t)

        for i in list_video:
            url_2='https://www.douyin.com/video/'+i
            pool.submit(getresult,url_2)
    print("over!!!")

#chrome.exe --remote-debugging-port=9527 --user-data-dir=“D:\AutomationProfile”

