BOT_NAME = "bewertung"

SPIDER_MODULES = ["bewertung.spiders"]
NEWSPIDER_MODULE = "bewertung.spiders"

ROBOTSTXT_OBEY = True

#PROXY_POOL_ENABLED = True

CUNCURRENT_REQUEST = 1

#SCRAPEOPS_API_KEY = '2fe431bf-9f9f-4ef9-ba02-dfe257fbaa93'

#SCRAPEOPS_PROXY_ENABLED = True

#DOWNLOADER_MIDDLEWARES = {
#    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
#}

#USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


#DOWNLOAD_HANDLERS = {
#    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#}

#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_selenium.SeleniumMiddleware': 800
#}



#PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True,}