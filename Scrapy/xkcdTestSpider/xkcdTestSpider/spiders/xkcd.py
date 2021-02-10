import scrapy
import re # ayyyy yiss REGEX BABY!!!
from ..items import XkcdtestspiderItem
# manual interactions
# class PostsSpider(scrapy.Spider):
#     name = 'xkcdScraper'

#     start_urls = [
#         'https://xkcd.com/1/',
#         'https://xkcd.com/2/',
#         'https://xkcd.com/3'
#     ]
#     def parse(self,response):
#         page = response.url.split('/')[-1]
#         filename = 'postXKCD-%s.html' % page
#         with open(filename,'wb') as f: #writes(over) everythin in the file (doesn't append)
#             f.write(response.body)

# lesson learned
# for div ids use #

#how to get the title of the comic
# response.css('#middleContainer #ctitle::text').get()

# returns the entire div 
# response.css('#middleContainer #comic img').get()

# returns the the actual usage image link
# response.css('#middleContainer #comic img').re(r'imgs.+.jpg')



#extracting the hidden text of the comic
# response.css('#middleContainer #comic img').re(r'title="(.*?)"')

class PostsSpider(scrapy.Spider):
    
    

    name = 'xkcdScraper'
    start_urls = ['https://xkcd.com']
    def parse(self,response):

        comic = XkcdtestspiderItem()

        next_page = response.css('#middleContainer ul li a::attr(href)')[1].get()
        nextPageRegex = r'(\d+)'
        match = re.search(nextPageRegex,next_page)

        comic['comicTitle'] =  response.css('#middleContainer #ctitle::text').get()
        comic['comicNumber'] = int(match[0])
        #'image link' : response.css('#middleContainer #comic img').re(r'imgs.+.jpg'),
        comic['comicImageLink'] = response.css('#middleContainer #comic img::attr(src)').get()[2:]
        comic['comicHiddenText'] = response.css('#middleContainer #comic img').re(r'title="(.*?)"')
        
        #response.css('#middleContainer #comic img::attr(title)').get()

        
        yield comic

        #if we want to scrape the entire webpage
        #if next_page is not None:

        # we are using the comic # as a way to stop
        if int(match[0]) > 2378:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
