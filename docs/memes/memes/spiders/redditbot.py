# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import json
import logging
import requests
from datetime import datetime
import shutil
import os

script_path = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('quoteresult.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        response = requests.get(item['src'], stream=True)
        directory = f"{script_path}/images/{item['directory']}/"
        if not os.path.exists(directory):
            os.mkdir(directory)
        file_name = item['src'].split('/')[3].split('?')[0]
        with open(directory + file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return item

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com']
    start_urls = [
            'http://www.reddit.com/r/libertarianmeme/',
            'http://www.reddit.com/r/dankmemes',
            'https://www.reddit.com/r/memeeconomy'
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for image in response.xpath("//img[@alt='Post image']|//img[@id='image-element']"):
            yield {
                'src': image.attrib['src'],
                'directory': response.url.split('/')[4]
            }
        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


process = CrawlerProcess(settings={
    'LOG_LEVEL': logging.WARNING,
    'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1}, # Used for pipeline 1
    'FEED_FORMAT': 'json',
    'FEED_URI': 'reddit_libertarian.json'
})

process.crawl(RedditbotSpider)
process.start()
