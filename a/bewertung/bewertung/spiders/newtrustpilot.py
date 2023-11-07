import scrapy
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

class TrustpilotSpider(scrapy.Spider):
    name = "trustpilot123"

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'COOKIES_ENABLED': True,
        'FEEDS': {'trustpilot2.json': {'format': 'json', 'overwrite': True}},
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'de-DE,de;q=0.9',
            'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        },
        'DOWNLOAD_HANDLERS': {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        'TWISTED_REACTOR': "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        'PLAYWRIGHT_LAUNCH_OPTIONS': {"headless": True}
    }


    def start_requests(self):
        url = "https://at.trustpilot.com/review/tfbank.at"
        yield scrapy.Request(url=url,meta=dict(
            playwright = True,
            playwright_include_page = True,
            errback=self.errback,
        ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()

    async def parse(self, response):
        all_reviews = response.css(".styles_loadMoreLanguages__wonXg::attr(href)").get()
        last_page = response.css(".pagination_paginationEllipsis__4lfLO+ .pagination-link_item__mkuN3::attr(href)").get()
        if all_reviews:
            yield response.follow(response.urljoin(all_reviews), self.parse_start)
        elif last_page:
            yield {
                'last_page': last_page
            }
            yield response.follow(response.urljoin(last_page), self.parse)

    def parse_start(self, response):
        # Extract the review details from the page
        reviews = response.css('.styles_reviewCardInner__EwDq2')

        for review in reviews:
            
            name = review.css('a span.typography_appearance-default__AAY17::text').get()
            rating = review.css('.styles_reviewHeader__iU9Px img::attr(alt)').extract_first()
            title = review.css('.link_notUnderlined__szqki .typography_appearance-default__AAY17::text').extract_first()
            content = review.css('.typography_color-black__5LYEn::text').extract_first()

            #more_than_one = review.css('.styles_button__pwkHk').get()
            #if more_than_one:
                #yield {
                    #'name': name,
                    #







                    #
                #}

            yield {
                'name': name,
                'rating': rating,
                'title': title,
                'content': content,
            }

        next_page = response.css('a.pagination-link_next__SDNU4::attr(href)').get()
        if next_page:
            yield response.follow(response.urljoin(next_page), self.parse_start)