import json
import os
import time

import scrapy
from scrapy.http import Request
from Myscrapy.items import MyItem


class Zhihu_SelSpider(scrapy.Spider):
    name = 'zhihu_sel'
    allowed_domains = ['https://www.zhihu.com/']
    # allowed_domains = ['https://www.baidu.com']
    start_urls = ['https://www.zhihu.com/']

    def parse(self, response):
        pass


    def start_requests(self):
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

        }

        cookies = {
            'KLBRSID':'81978cf28cf03c58e07f705c156aa833|1626334472|1626334263',

        }

        # Request(url=self.start_urls[0],headers=headers,cookies=)


        # #使用selenium登录
        # from selenium import webdriver
        # browser = webdriver.Chrome(executable_path='F:/pythonProject/pubilcVenv/seleniumDriver/chrome 91/chromedriver.exe')
        # browser.get('https://www.zhihu.com/')
        #
        # # 账户密码登录
        # time.sleep(5)
        # Cookies = browser.get_cookies()
        # # to file and dic
        # Cookies_dic = {}
        # if not os.path.exists('./cookies'):
        #     os.mkdir('./cookies')
        # for cookie in Cookies:
        #     with open('./cookies//'+cookie['name']+cookie['value']+'.txt','w') as f:
        #         json.dump(cookie,f)
        #         Cookies_dic[cookie['name']] = cookie['value']
        # print(Cookies_dic)
        # yield Request(url=self.start_urls[0],dont_filter=True,cookies=Cookies_dic)

    def back(self,response):
        pass