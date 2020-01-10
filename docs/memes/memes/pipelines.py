# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import requests
import shutil

class MemesPipeline(object):
    def open_spider(self, spider):
        # self.file = open('quoteresult.jl', 'w')
        pass

    def close_spider(self, spider):
        # self.file.close()
        pass

    def process_item(self, item, spider):
        script_path = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        response = requests.get(item['src'], stream=True)
        directory = f"{script_path}/images/{item['directory']}/"
        if not os.path.exists(directory):
            os.mkdir(directory)
        file_name = item['src'].split('/')[3].split('?')[0]
        with open(directory + file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return item

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        # self.file = open('quoteresult.jl', 'w')
        pass

    def close_spider(self, spider):
        # self.file.close()
        pass

    def process_item(self, item, spider):
        script_path = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        response = requests.get(item['src'], stream=True)
        directory = f"{script_path}/images/{item['directory']}/"
        if not os.path.exists(directory):
            os.mkdir(directory)
        file_name = item['src'].split('/')[3].split('?')[0]
        with open(directory + file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return item
