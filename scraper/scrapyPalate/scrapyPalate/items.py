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


# Item used to store Image objects
class Image(scrapy.Item):
    restaurant_id = scrapy.Field()
    image_id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    storage = scrapy.Field()
    pass