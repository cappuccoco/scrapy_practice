# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .utils.dao import Dao

class MyscrapyPipeline:
    def process_item(self, item, spider):
        print(item['title'],item['url'],item['id'])
        try:
            dao = Dao()
            sql = "insert into csdndata values (%s,%s,%s,%s)"
            dao.execute(sql, [item['id'][0], item['url'][0], item['title'][0], item['text'][0]])
            dao.commit()
            dao.close()
        except Exception as e:
            print("写入数据库失败"+str(e))

        return item



# class MyPipeline(ImagesPipeline):
#     def item_completed(self, results, item, info):
#         pass
#         pass