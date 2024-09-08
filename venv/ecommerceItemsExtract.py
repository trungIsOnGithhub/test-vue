import scrapy

class EcommerceitemsextractSpider(scrapy.Spider):
    name = "ecommerceItemsExtract"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io"]

    def parse(self, response):
        fetch(start_urls)
