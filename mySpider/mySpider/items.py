# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


class MovieItem(scrapy.Item):
    # 电影名字
    name = scrapy.Field()
    # 电影信息
    info = scrapy.Field()
    # 评分
    rating = scrapy.Field()
    # 评论人数
    num = scrapy.Field()
    # 经典语句
    quote = scrapy.Field()
    # 电影图片
    img_url = scrapy.Field()
    