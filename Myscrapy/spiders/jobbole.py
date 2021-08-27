import json
import time

import scrapy
from scrapy.http import Request
from Myscrapy.items import MyItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    # allowed_domains = ['blog.jobbole.com']
    # allowed_domains = ['https://www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        print(response)
        yield Request(url='https://www.baidu.com',callback=self.back)
        pass


    def start_requests(self):
        from selenium import webdriver
        browser = webdriver.Chrome(executable_path='F:/pythonProject/pubilcVenv/seleniumDriver/chrome 91/chromedriver.exe')
        browser.get('')
        time.sleep(5)
        Cookies = browser.get_cookies()
        # to file and dic
        Cookies_dic = {}
        for cookie in Cookies:
            with open(''+cookie['name']+cookie['value']) as f:
                json.dump(cookie,f)
                Cookies_dic[cookie['name']] = cookie['value']
        return Request(url=self.start_urls[0],dont_filter=True,cookies=Cookies_dic)

    def back(self,response):
        myItem = MyItem()
        myItem['title'] = 'title'
        myItem['image_urls'] = ['https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png']
        response.meta.get('','')

        yield myItem