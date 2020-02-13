import scrapy

class MyScraper(scrapy.Spider):
    name = 'iga_scraper'
    url = 'https://www.iga.com.au/stores/#view=storelocator'
    