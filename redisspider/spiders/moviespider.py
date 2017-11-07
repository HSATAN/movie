# _*_ coding:utf8 _*_

from scrapy_redis.spiders import RedisCrawlSpider
from redisspider.items import MovieItem
from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor


class MovieSpider(RedisCrawlSpider):

    name = 'movie'

    rules = (Rule(LinkExtractor(allow='movie\/\d+.html'), callback='parse_item'),)

    def parse_item(self, response):
        item = MovieItem()
        sel = Selector(response)
        item["movie_name"] = sel.xpath('//div[@class="col-xs-9 movie-info padding-right-5"]/h1/text()').extract()[0]
        item['movie_url'] = response.url
        return dict(item)