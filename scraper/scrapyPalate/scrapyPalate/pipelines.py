# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
import os

class ScrapypalatePipeline(object):
    def process_item(self, item, spider):
        # Image object is ready for downloading
        print('PROCESSING')
        print(item)
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # Request Image url for download
        print('MEDIA REQUEST STARTED')
        print(item)
        print('MEDIA REQUEST COMPLETE')
        yield Request(item['image_urls'])

    def item_completed(self, results, item, info):
        # Image has been downloaded and details are in...
        # Results = [( <Bool: did it get downloaded>, { 'url': <link>, 'path': <path to file>, 'checksum':<checksum>})]
        # Item = corresponding image item
        # TODO: Concatenate images into .rec file
        # TODO: Upload photos to AWS S3
        print('ITEM COMPLETED STARTED')
        print('RESULT')
        print(results)
        print(results[0][1]['path'])
        print('ITEM')
        print(item)
        print('ITEM COMPLETED COMPLETE')
        return item
