import scrapy
import json

class yelpSpider(scrapy.Spider):
    name = 'yelpSpider'

    def start_requests(self):

        API_Key = 'ph4AR6uxYuKLznMtCVxMcUrYzgVPhigppJAtwmlCt9Bybh2LRwJ-tP-eXGxaqlPQZaSfwhX7WblC05XCdd20Cyu5DUubbf-Uca-28rttk1YZHDVgBFZHHezDaAiNWnYx'

        BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'
        SEARCH_PARAMS = '?term=restaurants&location=los angeles'

        BUSINESS_PHOTOS_URL = 'https://www.yelp.com/biz_photos/'
        PHOTO_PARAMS = '?tab=food'

        scrapy.Request( url=BUSINESS_SEARCH_URL + SEARCH_PARAMS,
                        headers={'Authorization': 'Bearer ' + API_Key},
                        callback=self.Jparse)

    def parse(self, response):
        url = response.url
        url2 = url.replace("biz", "biz_photos")
        print("First URL is: " + url)
        print("Second URL is: " + url2)

    def Jparse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        ids = jsonresponse['id']

        for id in ids
            yield scrapy.Request(url=BUSINESS_PICS_URL + id + PHOTOPARAMS,
                                 callback=self.picPageParse())

    def picPageParse(self, response):
        response



