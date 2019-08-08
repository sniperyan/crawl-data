# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from mySpider.settings import MYSQL_HOST
from mySpider.settings import MYSQL_DBNAME
from mySpider.settings import MYSQL_USER
from mySpider.settings import MYSQL_PASSWD

class MyspiderPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8mb4')

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into teacher(name, title, info)
                value (%s, %s, %s)""",
                (item['name'],
                 item['title'],
                 item['info']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)

        return item

