# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def method1(value):
    return value


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MyItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(method1),
        output_processor=TakeFirst()
    )
    text = scrapy.Field()
    image_urls = scrapy.Field()


# csdn 的 blog 文章
class CsdnBlogItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    crawl_time = scrapy.Field()
