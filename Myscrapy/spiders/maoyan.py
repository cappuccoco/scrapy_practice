import json
import re
import time

import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Myscrapy.items import MyItem
from urllib import parse
from Myscrapy.items import CsdnBlogItem




class CsdnSpider(scrapy.Spider):
    name = 'maoyan'
    # allowed_domains = ['blog.jobbole.com']
    # allowed_domains = ['https://www.csdn.net/']
    start_urls = ['https://maoyan.com/']

    #
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        # 'Referer':'https://www.csdn.net/nav/python',
        'host':'https://maoyan.com/'
    }

    def parse(self, response):
        """"
        是films/数字的就进入进行爬取内容
        不是的就点进去
        """
        urls = response.xpath(r"//a/@href").extract()
        urls = [parse.urljoin(response.url,url) for url in urls]
        for url in urls:
            if 'films/' in url:
                # 进行爬取film的url
                yield Request(url ,callback=self.film)
            # else:
            #     # 继续url分析
            #     yield Request(url ,headers=self.headers,callback=self.parse)


    # 爬取blog内容
    def film(self,response):
        # itemloader = ItemLoader(item=CsdnBlogItem(),response=response)
        # itemloader.add_xpath('title',r"//h1[@class = 'title-article']")
        # itemloader.add_xpath('text',r"//div[@id='content_views']")
        # itemloader.add_value('url',response.url)
        #
        # return itemloader.load_item()
        print(response.text)
        print(response.url,'OK')

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, dont_filter=True,headers=self.headers)

    # def back(self,response):
