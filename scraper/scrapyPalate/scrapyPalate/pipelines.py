# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3


class ScrapypalatePipeline(object):



    filename = 'testRAMA'
    filename_ext = '.txt'
    bucket_name = 'palate'
    main_folder = 'photos/restaurants/'

    def process_item(self, item, spider):
        print('PROCESSING')
        print(item['id'])
        print(item['link'])
        s3 = boto3.client('s3')

        pics = item['pics']

        s3.upload_file('https://s3-media3.fl.yelpcdn.com/bphoto/tc38fJpwBMca52RVmLzc4A/o.jpg',
                       self.bucket_name, self.main_folder + 'testImage.jpg')

        return item
