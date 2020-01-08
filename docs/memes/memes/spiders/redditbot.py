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
        img_file = script_path + "/images/" + item['src'].split('/')[3].split('?')[0]
        with open(img_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return item

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/libertarianmeme']

    def start_requests(self):
        url = ['http://www.reddit.com/r/libertarianmeme/']
        yield scrapy.Request(url[0], self.parse)

    def parse(self, response):
        for image in response.xpath("//img[@alt='Post image']"):
            yield {'src': image.attrib['src'] }

process = CrawlerProcess(settings={
    'LOG_LEVEL': logging.WARNING,
    'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1}, # Used for pipeline 1
    'FEED_FORMAT': 'json',
    'FEED_URI': 'reddit_libertarian.json'
})

process.crawl(RedditbotSpider)
process.start()
