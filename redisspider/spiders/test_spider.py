# _*_ coding: utf8 _*_

from __future__ import print_function
from scrapy_redis.spiders import RedisSpider
from redisspider.items import RedisspiderItem


class TestSpider(RedisSpider):

    name = 'testspider'

    def parse(self, response):
        print(response.text)
        item = RedisspiderItem()
        item['name'] = 'huagnkaijie'
        return item