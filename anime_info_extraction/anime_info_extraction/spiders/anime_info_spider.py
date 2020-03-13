# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:57:54 2019

@author: mam22
"""

import scrapy
import pandas as pd
from ..items import AnimeInfoExtractionItem
class AnimeInfoSpider(scrapy.Spider):
    
    name ='anime_info'
    urls = pd.read_csv('links.csv')['link'].tolist()
    start_urls =[url+'/characters' for url in urls]
    
    def parse(self,response):
        item = AnimeInfoExtractionItem()
        item['anime_id']=int(response.url.split('/')[4])
        item['anime_name']=response.css('h1 span::text').get()
        item['character_names']=response.css("td >a[href*='character']::text").extract()
        item['id']=response.css("td >a[href*='character']::attr(href)").extract()
        yield item