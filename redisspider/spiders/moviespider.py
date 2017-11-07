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
        item["name"] = sel.xpath('//div[@class="col-xs-9 movie-info padding-right-5"]/h1/text()').extract()[0]
        item['url'] = response.url
        datatable = sel.xpath('//table[@class="table table-striped table-condensed table-bordered"]'
                              '/tbody')
        item['director'] = datatable.xpath('./tr[1]/td[2]//a//text()').extract()[0]
        item['playwright'] = ','.join(datatable.xpath('./tr[2]//a//text()').extract())
        item['star'] = ','.join(datatable.xpath('./tr[3]//a//text()').extract())
        item['type'] = ','.join(datatable.xpath('./tr[4]//a//text()').extract())
        item['address'] = ','.join(datatable.xpath('./tr[5]//a//text()').extract())
        item['language'] = datatable.xpath('./tr[6]//td[2]//text()').extract()[0]
        #item['time'] = datatable.xpath('./tr[7]//text()').extract()[0]
        #item['long'] = datatable.xpath('./tr[8]//text()').extract()[0]
        #item['douban_score'] = datatable.xpath('./tr[9]//a[1]//text()').extract()[0]
        return dict(item)