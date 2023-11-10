import scrapy


class AmazoncomSpider(scrapy.Spider):
    name = "amazoncom"
    def __init__(self, *args, **kwargs): 
        super(AmazoncomSpider, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_url')] 
    #start_urls = ["https://www.amazon.de/TECKNET-Business-Verdrahtete-Ergonomische-Verstellbare/dp/B0887X29QJ/ref=sr_1_16?crid=EZMZXS1655L5&keywords=computer+maus&qid=1695560831&sprefix=%2Caps%2C73&sr=8-16"]

    custom_settings = {
        'FEEDS': {'..\\amazon.json': {'format': 'json', 'overwrite': True}},
        'DEFAULT_REQUEST_HEADERS': {
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'de',
            'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
        },
    }

    def parse(self, response):
        ret = response.css('#reviews-medley-footer .a-text-bold').attrib['href']
        if ret:
            yield response.follow(response.urljoin(ret), self.parse_ret)
        else: 
            yield {"text": "No Produkt page"}

    def parse_ret(self, response):
        for produkts in response.css("#cm_cr-review_list .celwidget:not(#cm_cr-pagination_bar)"):
            profile_names = produkts.css('.a-profile-name::text').get()
            ratings = produkts.css('.a-text-bold span:not(.a-icon-alt):not(.a-letter-space)::text').get()
            rating_icons = produkts.css('.a-text-bold span.a-icon-alt::text').get()
            review_texts = produkts.css('.review-text-content span::text').get()
            review_states = produkts.css('.a-color-state::text').get()
            
        
            # You can process and yield the extracted data here
            yield {
                'profile_names': profile_names,
                'ratings': ratings,
                'rating_icons': rating_icons,
                'review_texts': review_texts,
                'review_states': review_states,
            }
        
        next_page = response.css('.a-last a::attr(href)').get()
        if next_page:
            yield response.follow(response.urljoin(next_page), self.parse_ret)
