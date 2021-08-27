from scrapy.cmdline import execute
import sys
import os
# 添加项目目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 调用execute来执行命令行命令
execute(["scrapy","crawl","csdn"])	#命令行 scrapy crawl jobbole 最后一个是爬虫的文件名





