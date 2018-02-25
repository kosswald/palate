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


class Image(scrapy.Item):
    restaurant_id = scrapy.Field()
    image_id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    #session_path = scrapy.Field()
    pass


class Restaurant(scrapy.Item):
    id = scrapy.Field()
    imgs = scrapy.Field()
    pass