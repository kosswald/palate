import scrapy
import json

class yelpSpider(scrapy.Spider):
    name = 'yelpSpider'

    API_Key = 'ph4AR6uxYuKLznMtCVxMcUrYzgVPhigppJAtwmlCt9Bybh2LRwJ-tP-eXGxaqlPQZaSfwhX7WblC05XCdd20Cyu5DUubbf-Uca-28rttk1YZHDVgBFZHHezDaAiNWnYx'

    BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'
    SEARCH_PARAMS = '?term=restaurants&location=los angeles'

    BUSINESS_PHOTOS_URL = 'https://www.yelp.com/biz_photos/'
    PHOTO_PARAMS = '?tab=food'

    PHOTO_LINK = 'https://s3-media3.fl.yelpcdn.com/bphoto/'
    PHOTO_EXT = '/o.jpg'

    def start_requests(self):

        print(self.BUSINESS_SEARCH_URL + self.SEARCH_PARAMS)
        request = scrapy.Request(url=self.BUSINESS_SEARCH_URL + self.SEARCH_PARAMS,
                                 headers={'Authorization': 'Bearer ' + self.API_Key},
                                 method='GET',
                                 callback=self.Jparse)
        return [request];

    def parse(self, response):
        url = response.url
        print("First URL is: " + url)

    def Jparse(self, response):
        try:
            print('JPARSE REACHED')
            jsonresponse = json.loads(response.body_as_unicode())
            print(jsonresponse['businesses'][0]['id'])

            totalResponse = jsonresponse['total']
            idList = []

            print('LOOP REACHED')
            for business in jsonresponse['businesses']:
                idList.append(business.get('id'))

            for id in idList:
                print(id)
                yield scrapy.Request(url=self.BUSINESS_PHOTOS_URL + id + self.PHOTO_PARAMS,
                                     callback=self.picPageParse)

        except:
            print('JPARSE FAILED')

    def picPageParse(self, response):

        print('PICPARSEREACHED')
        picture_class = 'photo-box-img'
        gallery_class = 'media-landing_gallery photos'
        pic_id = '@data-photo-id'

        pic_ids = []

        # xpath to element in gallery // *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul / li[1]
        # xpath to gallery // *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul

        print(response.xpath('// *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul / li').xpath(pic_id).extract())
        pic_ids = response.xpath('// *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul / li').xpath(pic_id)

        for id in pic_ids:
            link = self.PHOTO_LINK + id.extract() + self.PHOTO_EXT
            print(link)





