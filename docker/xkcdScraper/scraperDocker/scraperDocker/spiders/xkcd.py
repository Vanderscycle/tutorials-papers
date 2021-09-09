import scrapy
import re
from ..items import xkcdComicElement

'''
docker run -d -p 27017:27017 -v /data/bin:/data/db  --name mango mongo # runs the mongo container and save locally (important for docker compose) port 127.0.0.1:27017
'''

class xkcdSpider(scrapy.Spider):
    # class variables
    name = 'xkcdDocker'
    allowed_domains = ["xkcd.com"]
    # specific settings for the spider
    custom_settings = {
        'ITEM_PIPELINES' : {
    'scraperDocker.pipelines.xkcdMongoDBStorage': 200,
    #'scraperDocker.pipelines.xkcdComicItemPipeline': 300,
        }
    }
    def start_requests(self): 
        start_url = 'https://xkcd.com'
        yield scrapy.Request(url=start_url, callback=self.homepageComic)

    def homepageComic(self,response):
        """
        In the current format we will skip the first comic. The goal being that we start at the homepage
        before going backward.
        Input:
            initial reponse from start_requests 
        Output:
            response to comicPages method
        """
        self.logger.info(f'------- homepage -------')
        # moving backward
        nextPage = response.css('li:nth-child(2) a::attr(href)')[1].get() #prev button
        nextPageRegex = r'(\d+)'
        match = re.search(nextPageRegex,nextPage)
        nextPage = response.urljoin(nextPage)
        yield scrapy.Request(url=nextPage , callback=self.comicPages)
    
    def comicPages(self,response):
        """
        This method scrape the desired comic field except the very first one skipped from homepage.
        Input:
            reponse from homepageComic
        Output
            response looping back to comicPages. Stop
        """
        self.logger.info(f'------- XKCD comic number {response} -------')

        # next page url and comic number extraction
        nextPage = response.css('li:nth-child(2) a::attr(href)')[1].get()
        nextPageRegex = r'(\d+)'
        match = re.search(nextPageRegex,nextPage)

        currentComicElements = xkcdComicElement()        
        currentComicElements['comicTitle'] = response.css('#ctitle::text').get()
        currentComicElements['comicNumber'] = match[0] 
        currentComicElements['imgUrl'] = str(response.css('#comic img::attr(src)').get())[2:] # doesn't fetch the img
        currentComicElements['hiddenText'] = response.css('#comic img::attr(title)').get()
        # future improvement could be to categorize each comic (computer,love,etc.)

        yield currentComicElements
        # next page
        nextPage = response.urljoin(nextPage)

        # if nextPage is not None:
        if int(match[0]) >= 2397:
            yield scrapy.Request(nextPage,callback=self.comicPages)
