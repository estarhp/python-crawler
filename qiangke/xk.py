from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time

from concurrent.futures import ThreadPoolExecutor

import os

def click(i):
    web.get('http://xk1.cqupt.edu.cn/yxk.php')
    while i > -1:


        web.find_element('xpath', '/html/body/div[3]/div[2]/ul/li[1]/ul/li[2]/a').click()

        # js = "var q=document.documentElement.scrollTop=4000"
        # web.execute_script(js)
        time.sleep(0.1)
        n = i % 22 + 92

        try:
            web.find_element('xpath', f'/html/body/div[3]/div[1]/div/div/form/table/tbody/tr[{n}]/td[5]').click()
            time.sleep(0.3)
            a = web.switch_to.alert
            print(a.text)
            a.accept()
            i += 1
        finally:
            i+=1
            click(i)








if __name__ == '__main__':

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    web = webdriver.Chrome(options=options)
    click(0)








