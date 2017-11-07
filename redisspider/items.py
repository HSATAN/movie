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

    movie_name = scrapy.Field()
    movie_url = scrapy.Field()
