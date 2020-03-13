# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


import scrapy
import pandas as pd

class CharacterLinkSpider(scrapy.Spider):
    
    name ='character_link'
    urls = pd.read_csv('links.csv')['link'].tolist()
    start_urls =[url+'/characters' for url in urls]
    
    def parse(self,response):
        character_links = response.css("td >a[href*='character']::attr(href)").extract()
        if len(character_links) > 0:
                for character_link in character_links:
                    yield {'character_link':character_link}