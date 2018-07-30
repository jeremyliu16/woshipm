# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from items import WoshipmItem


class WoshipmMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Woshipm"]
        self.PhRes = db["PmRes"]

    def process_item(self, item, spider):
        print 'MongoDBItem', item
        """ 判断类型 存入MongoDB """
        if isinstance(item, WoshipmItem):
            print 'PmArticleItem True'
            try:
                self.PhRes.insert(dict(item))
                print 'Insert successfully'
            except Exception:
                pass
        return item
