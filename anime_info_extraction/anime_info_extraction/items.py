# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeInfoExtractionItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    anime_name = scrapy.Field()
    anime_id = scrapy.Field()
    character_names = scrapy.Field()
    
