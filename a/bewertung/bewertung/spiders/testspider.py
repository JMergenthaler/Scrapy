

import scrapy
from scrapy_selenium import SeleniumRequest

class MySpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(url="https://example.com", callback=self.parse)

    def parse(self, response):
        # Use Selenium to interact with the page and extract data
        pass
