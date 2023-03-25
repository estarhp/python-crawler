import re
import requests
import os
os.chdir(r'D:\Desktop\从抖音爬到的视频')
url='https://www.douyin.com/video/7163279309791120681'
headers={
    'cookie': 'douyin.com; ttwid=1%7C4PfqWzjTeZsLO8zyYOzLf7CQby5DcNN4zkSThvcCoVM%7C1660557974%7C9c9794fe7933189cf94bebb246397beaa594887d738b13218b13e820797e5412; strategyABtestKey=1660557976.692; s_v_web_id=verify_l6ulcfbf_5KJ83orR_O3sM_42dH_BvCc_nEnF9RzcHjbc; passport_csrf_token=9072f640080f068c03d59db60d30cc54; passport_csrf_token_default=9072f640080f068c03d59db60d30cc54; ttcid=c425c71e5a5240f496105458282b00da18; n_mh=0Nq0PtRnjxLi1K3bqi9jIyTqihwy5Eelyhf0BFF9bM0; sso_uid_tt=de6fd5b6fe99474b61a875d1e749fc96; sso_uid_tt_ss=de6fd5b6fe99474b61a875d1e749fc96; toutiao_sso_user=57490f73895f175fb1a905390c296ea6; toutiao_sso_user_ss=57490f73895f175fb1a905390c296ea6; sid_ucp_sso_v1=1.0.0-KGNkZDQ3Y2UwM2YwM2MxNzY5YmJlMmQxNDQyYjVjZTgwYzkyMTgxNmUKHQj_uODV3gIQtbXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; ssid_ucp_sso_v1=1.0.0-KGNkZDQ3Y2UwM2YwM2MxNzY5YmJlMmQxNDQyYjVjZTgwYzkyMTgxNmUKHQj_uODV3gIQtbXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; odin_tt=7e4bb327515c33b6f87ade3aad50f19c6323350e395994565f2b55ea40f1039d1c0cf240ef0fef412f803b945978d11e; sid_guard=57490f73895f175fb1a905390c296ea6%7C1660558006%7C5184000%7CFri%2C+14-Oct-2022+10%3A06%3A46+GMT; uid_tt=de6fd5b6fe99474b61a875d1e749fc96; uid_tt_ss=de6fd5b6fe99474b61a875d1e749fc96; sid_tt=57490f73895f175fb1a905390c296ea6; sessionid=57490f73895f175fb1a905390c296ea6; sessionid_ss=57490f73895f175fb1a905390c296ea6; sid_ucp_v1=1.0.0-KGE4YzllNjQ2MmI1M2I0Zjg4MGM1ZTYwYjE2NWFmNTdlMjk1MzZhYjUKHQj_uODV3gIQtrXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; ssid_ucp_v1=1.0.0-KGE4YzllNjQ2MmI1M2I0Zjg4MGM1ZTYwYjE2NWFmNTdlMjk1MzZhYjUKHQj_uODV3gIQtrXolwYY7zEgDDCy1NjUBTgGQPQHGgJsZiIgNTc0OTBmNzM4OTVmMTc1ZmIxYTkwNTM5MGMyOTZlYTY; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAHiF_1qLSnSkvrBJtTnwyrQEMnKWvypI9JjFDRQ2yOE8%2F1660579200000%2F0%2F1660558009912%2F0%22; _tea_utm_cache_1243=undefined; THEME_STAY_TIME=%22299396%22; IS_HIDE_THEME_CHANGE=%221%22; __ac_nonce=062fa389800a44c2dcf95; __ac_signature=_02B4Z6wo00f01piVOogAAIDAeiBKHgjOemqYpT4AAMTrKiQp1RkAYe6lguL33R6pIM0RqBqs8DtSkMHIxEyD8pdQiFiUYc7lCzXIBjB.b4lnaAnocgazVzkrNnNrY4izenlrnfR9eDX.Hvdv14; MONITOR_WEB_ID=088b39e1-7e30-4218-8d14-2c6625410fa3; douyin.com; msToken=0fJfq4xf6t8mwrit4O29j7K_FGynpJEGidTFm277js9UbkUbN3FA89AT4W1I_crGfwugtkD6G4eNCY9mG9DLAHJFcHlWXrv9lrf9mIw2k6DduN7HknULpA==; home_can_add_dy_2_desktop=%221%22; msToken=rDP9A2hqh5xL-WDQEbNhC3u5ilkEV1JTG37gjLVlwGObEBBBm6wVu-GNqDwfDcwwIe84mvIu8ave11F-WXv28zQ0Q6O-mBR4FIhxBCVkBB3tQDxvMZzSPz_iluIJ15c=; tt_scid=uDo7yqeK6-Qdpy5wCwHnhzi4-EEg2udJ6eMZSpUbZ.dcZKUmgsOx0ocD5wSlc-sq4c77',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
    }
response=(requests.get(url=url,headers=headers))
title=re.findall('<title data-react-helmet="true">(.*?)- 抖音</title>',response.text,re.S)[0]
html_data=re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script',response.text,re.S)[0]
html_data=requests.utils.unquote(html_data)
import json
from pprint import pprint
json_data=json.loads(html_data)
pprint(json_data)
vd_url='https:'+json_data['32']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
vd_content=requests.get(url=vd_url,headers=headers).content
with open('抖音-'+'.mp4','wb') as f:
    f.write(vd_content)
response.close()