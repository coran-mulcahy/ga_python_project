import scrapy

class StoreSpider(scrapy.Spider):
    name = 'scraper'
    start_urls = ['https://www.iga.com.au/stores/#view=storelocator']

    def parse(self, response):

        store_name = response.xpath("//span[@class='sf-storename']/text()").extract()
        store_address = response.xpath("//p[@class='sf-storeaddress']/text()").extract()
        yield {
           'store_name' : store_name,
            'store_address' : store_address
        }