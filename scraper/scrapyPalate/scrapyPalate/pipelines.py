# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3 as boto
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request


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

        pic_storage = results[0][1]['path']
        pic_name = item['image_id']
        pic_restaurant = item['restaurant_id']
        image_store = item['storage']

        local_path_to_image = image_store + pic_storage
        bucket_path_to_image = 'photos/restaurants/' + pic_restaurant + '/' + pic_name + '.jpg'
        metadata = {'ContentType': 'image/jpeg', 'ACL': 'public-read'}

        s3 = boto.resource('s3')
        bucket = 'palate'
        s3.meta.client.upload_file(local_path_to_image, bucket, bucket_path_to_image, metadata)

        print('ITEM COMPLETED STARTED')
        print('RESULT')
        print(results)
        print(results[0][1]['path'])
        print('Restaurant ID: ' + pic_restaurant)
        print('IMAGE STORE PATH: ' + image_store + pic_storage)
        print('ITEM')
        print(item)
        print('ITEM COMPLETED COMPLETE')
        return item
