# _*_ coding:utf8 _*_

from scrapy_redis.spiders import RedisCrawlSpider
from redisspider.items import MovieItem
from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import scrapy


class SheBaoSpider(scrapy.Spider):

    def start_requests(self):
        yield scrapy.Request()
        pass