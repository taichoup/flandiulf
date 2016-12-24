# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AstrocrawlItem(scrapy.Item):
    # define the fields for your item here like:
    lang = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    love = scrapy.Field()
    money = scrapy.Field()
    health = scrapy.Field()
    work = scrapy.Field()
    timestamp = scrapy.Field(serializer=str)
    source = scrapy.Field(serializer=str)
    sign = scrapy.Field(serializer=str)