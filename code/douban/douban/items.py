# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    # 电影名
    movie_name = scrapy.Field()
    # URL
    url = scrapy.Field()
    # 电影详情信息
    info = scrapy.Field()
    # 电影评分信息
    rating = scrapy.Field()
