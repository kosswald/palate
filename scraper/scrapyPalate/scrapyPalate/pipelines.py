# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import boto3

from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
import os

class ScrapypalatePipeline(object):
    def process_item(self, item, spider):
        print('PROCESSING')
        print('IMAGE_ID: ' + item['image_id'])
        print('IMAGE_URL: ' + item['image_urls'])
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('MEDIA REQUEST STARTED')
        print(item)
        print('MEDIA REQUEST COMPLETE')
        yield Request(item['image_urls'])

    def item_completed(self, results, item, info):
        print('ITEM COMPLETED STARTED')
        print('RESULT')
        print(results)
        print('ITEM')
        print(item)
        print('ITEM COMPLETED COMPLETE')
        return item

    def map_items(self, results, item):
        # TODO: Map out all the images into a json file
        print('RESULT')
        print(results)
        print('ITEM')
        print(item)