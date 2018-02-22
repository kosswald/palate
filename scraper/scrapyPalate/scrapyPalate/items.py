# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapypalateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Picture(scrapy.Item):
    # define the fields for your
    id =scrapy.Field()
    file_urls = scrapy.Field()
    #stored_at = scrapy.Field()
    pass

class Restaurant(scrapy.Item):
    id = scrapy.Field()
    link = scrapy.Field()
    pics = scrapy.Field()
    pass