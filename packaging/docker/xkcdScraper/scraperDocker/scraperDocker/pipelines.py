from scrapy.exceptions import DropItem
# scrappy log is deprecated
#from scrapy.utils import log
import logging
import scrapy
from itemadapter import ItemAdapter
import pymongo

class xkcdMongoDBStorage:
    """
    Class that handles the connection of 
    Input:
        nil
    Output
        nil
    """
    def __init__(self):
        # requires two arguments(address and port)
        #* connecting to the db
        self.conn = pymongo.MongoClient(host='NoSQLDB',port=27017,username='root',password='password',authSource="admin")

        #self.conn = pymongo.MongoClient(
         #   '127.0.0.1',27017) # works with spider local and container running

        # connecting to the db
        dbnames = self.conn.list_database_names()
        if 'randallMunroe' not in dbnames:
            # creating the database
            self.db = self.conn['randallMunroe']

        #if database already exists we want access
        else:
            self.db = self.conn.randallMunroe
        #* connecting to the table
        dbCollectionNames = self.db.list_collection_names()
        if 'webComic' not in dbCollectionNames:
            self.collection = self.db['webComic']
        
        else:
            # the table already exist so we access it
            self.collection = self.db.webComic

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.info(f"Question added to MongoDB database!")
        return item


class xkcdComicItemPipeline:
    def process_item(self, item, spider):
        # confirming that the item scraped from the spiders make their way inside the pipeline
        print(spider)
        for k,v in item.items():
            print(f'key/value: {k} : {v}')

        return item
