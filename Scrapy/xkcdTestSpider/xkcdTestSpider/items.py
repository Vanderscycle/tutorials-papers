# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XkcdtestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field
    comicTitle = scrapy.Field()
    comicNumber = scrapy.Field()
    comicImageLink = scrapy.Field()
    comicHiddenText = scrapy.Field()

