# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()


class MovieItem(scrapy.Item):

    name = scrapy.Field()
    url = scrapy.Field()
    playwright = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    language = scrapy.Field()
    long = scrapy.Field()
    douban_score = scrapy.Field()
    intro = scrapy.Field()
    tags = scrapy.Field()
    source = scrapy.Field()
    time = scrapy.Field()
