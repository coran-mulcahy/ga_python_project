import scrapy

class StoreSpider(scrapy.Spider):
    name = 'iga_scraper'
    start_urls = [
        'https://www.iga.com.au/stores/#view=storelocator'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}