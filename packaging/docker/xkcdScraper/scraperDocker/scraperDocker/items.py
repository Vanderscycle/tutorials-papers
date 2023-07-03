# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class xkcdComicElement(scrapy.Item):

    comicTitle = scrapy.Field()
    comicNumber = scrapy.Field()
    imgUrl = scrapy.Field()
    hiddenText = scrapy.Field()
