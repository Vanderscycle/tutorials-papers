# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class XkcdtestspiderPipeline:

    def __init__(self):
        # requires two arguments
        self.conn = pymongo.MongoClient(
            '127.0.0.1',
            27017
            )
        # creating the database
        db = self.conn['randallMunroe']
        # creating a table
        self.collection = db['webComic']


    def process_item(self, item, spider):
        
        self.collection.insert_one(dict(item))

        # testing
        # for k,v in item.items():
        #     print(f'pipeline key: {k}; value: {v}')
        return item
