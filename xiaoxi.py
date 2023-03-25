from selenium.webdriver import Chrome
import time
from douyin_img import download
from concurrent.futures import ThreadPoolExecutor
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
    js = "var q=document.documentElement.scrollTop=10000"
    web.execute_script(js)

if __name__ == '__main__':

    web=Chrome()

    web.get("https://www.douyin.com/user/MS4wLjABAAAAgM29WYvcRAVFEbkQ8xuMoeKxCIFPVyoioMa6NTfuyH0")
    time.sleep(2)
    web.find_element('class name', 'dy-account-close').click()
    xiala()
    list=web.find_elements('xpath','/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/ul/li/a')
    with ThreadPoolExecutor(200) as t:
        for i in list:
            t.submit(download, i.get_attribute("href"))
    print('搞定')