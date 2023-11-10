import re
import os
import scrapy
from scrapy.crawler import CrawlerProcess
from bewertung.spiders.amazon_ue_test import AmazonspiderSpider
from bewertung.spiders.trustpilot import TrustpilotSpider
from bewertung.spiders.amazoncom import AmazoncomSpider
from scrapy.utils.project import get_project_settings
import json

def run_spider_am(link):
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(AmazonspiderSpider, start_url=link) 
    process.start()

def run_spider_am_com(link):
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(AmazoncomSpider, start_url=link)
    process.start()

def run_spider_trust(link):
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(TrustpilotSpider, start_url=link)
    process.start()

def read_file():
    directory = "a\\bewertung\\json\\"

# Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        # Check if it's a file and not a directory (or use any other filter you need)
        if os.path.isfile(filepath):
            # Open and read the file
            with open(filepath, 'r') as f:
                data = json.load(f)
                if data:
                    link = data[0].get('link', '')
                    url = link
                else:
                    print("No data in the JSON.")
                    return

                regex = r"https:\/\/([\w.-]+)"

                match = re.search(regex, url)

                if match:
                    result = match.group(1)
                    regex_am_de = r"amazon.de"
                    match = re.search(regex_am_de, result)
                    regex_am_com = r"amazon.com"
                    match1 = re.search(regex_am_com, result)
                    regex_trust = r"trustpilot" 
                    match2 = re.search(regex_trust, result)
                    if match:
                        result = match.group()
                        run_spider_am(url)
                    elif match1:
                        result = match1.group()
                        run_spider_am_com(url) 
                    elif match2:
                        result = match2.group()
                        run_spider_trust(url)
                    else:
                        print("Nicht Supportet")
                else:
                    print("No match found.")

read_file()