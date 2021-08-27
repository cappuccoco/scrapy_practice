import json
import random
import re
import time

import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Myscrapy.items import MyItem
from urllib import parse
from Myscrapy.items import CsdnBlogItem




class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://www.csdn.net/']

    #
    # headers = {
    #
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #     'Accept-Encoding':'gzip, deflate, br',
    #     'Connection': 'keep-alive',
    #     'TE': 'Trailers',
    #     'Upgrade-Insecure-Requests':'1',
    #
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    #     'Referer':'https://www.csdn.net/',
    #     'host':'www.csdn.net',
    # }
    headers = {
        "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",

    }

    # cookies
    cookies = {
        'Accept':r'* / *',

    }

    def parse(self, response):
        """"
        是blog的就进入进行爬取内容
        不是blog的就点进去
        """
        urls = response.xpath(r"//a/@href").extract()
        urls = [parse.urljoin(response.url,url) for url in urls]
        for url in urls:
            if 'article' in url:
                # 进行爬取blog的url
                print(url)
                # time.sleep(random.randint(1,5))
                yield Request(url ,headers=self.headers,callback=self.blog)
                # # 从blog中继续爬取blog
                # yield Request(url, headers=self.headers, callback=self.parse)
            else:
                # 继续url分析
                yield Request(url ,headers=self.headers,callback=self.parse)


    # 爬取blog内容
    def blog(self,response):

        # try:
        #     rand = str(random.randint(0,1000))
        #     with open(rand +'.txt','w',encoding='utf-8') as f:
        #         # text = response.text
        #         # with open(rand +'m.txt','w',encoding='utf-8') as f:
        #         #     pass
        #         text = response.xpath(r"//div[@id='content_views']").extract()
        #         text_1 = text[0]
        #         f.write(text_1)
        #         pass
        # finally:
        #     pass

        itemloader = ItemLoader(item=CsdnBlogItem(),response=response)
        itemloader.add_xpath('title',r"//h1[@class = 'title-article']/text()")
        itemloader.add_xpath('text',r"//div[@id='content_views']")
        url = response.url
        itemloader.add_value('url',url)
        # 以detail的后边数字为id
        id = re.search(r'details/(\d*)?',url).group(1)
        itemloader.add_value('id',id)

        return itemloader.load_item()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True,headers=self.headers,cookies=None)

    # def back(self,response):
