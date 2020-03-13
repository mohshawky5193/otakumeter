



import scrapy
import pandas as pd
from ..items import CharacterImagesItem
class CharacterImageSpider(scrapy.Spider):
    
    name= 'character_image'
    start_urls = pd.read_csv('character-links.csv')['character_link'].drop_duplicates().sort_values().tolist()
    print(len(start_urls))
    def parse(self,response):
        image = response.css("a[href *='character'] img::attr(data-src)").extract()
        id = int(response.request.url.split('/')[4])
        item = CharacterImagesItem()
        item['character_image_link'] = image
        item['character_id']=id
        yield item