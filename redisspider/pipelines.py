# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import print_function
from redisspider.database.mysqldb import MysqlDB


class RedisspiderPipeline(object):

    def spider_open(self):
        print('starting--------------------------')

    def process_item(self, item, spider):
        keys = ""
        values = ""
        for key, value in dict(item).items():
            values += ",'%s'" % value
            keys += ",%s" % key
        values = values.strip(',')
        keys = keys.strip(',')
        print("insert into movie(%s) VALUES (%s)" % (keys, values))
        MysqlDB.insert("insert into movie(%s) VALUES (%s)" % (keys, values))
        return item
