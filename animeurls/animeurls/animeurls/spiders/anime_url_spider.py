
import scrapy

from ..items import AnimeurlsItem
import requests
class AnimeUrlSpider(scrapy.Spider):
    name ='anime'
    letter='A'
    show=0
    start_urls=['https://myanimelist.net/anime.php?letter='+letter+'&show='+str(show)]
    
    
    def parse(self,response):
        item = AnimeurlsItem()
        links = response.xpath("//a[@class='hoverinfo_trigger' and contains(@href,'anime')]/@href").extract()
        for link in links:
            item['link']=link;
            yield item
        AnimeUrlSpider.show +=50
        next_link ='https://myanimelist.net/anime.php?letter='+AnimeUrlSpider.letter+'&show='+str(AnimeUrlSpider.show)
        if (requests.get(next_link).status_code != 200):
            if AnimeUrlSpider.letter != 'Z':
                AnimeUrlSpider.letter = chr(ord(AnimeUrlSpider.letter)+1)
                AnimeUrlSpider.show = 0
                next_link ='https://myanimelist.net/anime.php?letter='+AnimeUrlSpider.letter+'&show='+str(AnimeUrlSpider.show)
                yield response.follow(next_link,callback = self.parse)
        else:
            yield response.follow(next_link,callback = self.parse)