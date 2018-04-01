# -*- coding: utf-8 -*-
import scrapy


# class ChoutiSpider(scrapy.Spider):
#     name = 'chouti'
#     allowed_domains = ['chouti.com']
#     start_urls = ['http://dig.chouti.com/']
#
#     def parse(self, response):
#         print(response)
import redis

redis.StrictRedis
from scrapy_redis.spiders import RedisSpider
class ChoutiSpider(RedisSpider):
    name = 'chouti'
    allowed_domains = ['chouti.com']

    def parse(self, response):
        print(response)

