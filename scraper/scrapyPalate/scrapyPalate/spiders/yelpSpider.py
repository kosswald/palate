import scrapy
import json
from scrapyPalate.items import Image
from scrapyPalate.items import Restaurant

class yelpSpider(scrapy.Spider):
    name = 'yelpSpider'

    # DELETE THIS KEY BEFORE MAKING REPO PUBLIC
    API_Key = 'ph4AR6uxYuKLznMtCVxMcUrYzgVPhigppJAtwmlCt9Bybh2LRwJ-tP-eXGxaqlPQZaSfwhX7WblC05XCdd20Cyu5DUubbf-Uca-28rttk1YZHDVgBFZHHezDaAiNWnYx'

    BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'
    SEARCH_PARAMS = '?term=restaurants&location=los angeles'

    BUSINESS_PHOTOS_URL = 'https://www.yelp.com/biz_photos/'
    BUSINESS_PHOTO_PARAMS = '?tab=food'

    PHOTO_LINK = 'https://s3-media3.fl.yelpcdn.com/bphoto/'
    PHOTO_EXT = '/o.jpg'


    def start_requests(self):
        print(self.BUSINESS_SEARCH_URL + self.SEARCH_PARAMS)
        return [scrapy.Request(url=self.BUSINESS_SEARCH_URL + self.SEARCH_PARAMS,
                                headers={'Authorization': 'Bearer ' + self.API_Key},
                                callback=self.Jparse)]

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
                request = scrapy.Request(url=self.BUSINESS_PHOTOS_URL + id + self.BUSINESS_PHOTO_PARAMS,
                                         callback=self.picPageParse)
                request.meta['item'] = {'id': id}
                yield request
        except:
            print('JPARSE FAILED')

    def picPageParse(self, response):

        print('PICPARSEREACHED')
        #picture_class = 'photo-box-img'
        gallery_class = 'media-landing_gallery photos'
        pic_id_xpath = '@data-photo-id'
        pic_xpath = '// *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul / li'
        pic_ids = []

        # xpath to element in gallery // *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul / li[1]
        # xpath to gallery // *[ @ id = "super-container"] / div[2] / div / div[2] / div[2] / ul

        print(response.xpath(pic_xpath).xpath(pic_id_xpath).extract())
        pic_ids = response.xpath(pic_xpath).xpath(pic_id_xpath)

        restaurant_id = response.meta['item']['id']
        print('RESTAURANT ID: ' + restaurant_id)

        for id in pic_ids:
            link = self.PHOTO_LINK + id.extract() + self.PHOTO_EXT
            pic = Image(restaurant_id=restaurant_id,
                        image_id=id.extract(),
                        image_urls=link)
            print('ID: ' + pic['image_id'])
            print('Link: ' + pic['image_urls'])
            yield pic

        #print(self.RESTAURANT_ID)
        #yield Restaurant(id=self.RESTAURANT_ID, imgs=pics)


