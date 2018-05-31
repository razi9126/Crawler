import scrapy
from scrapy.crawler import CrawlerProcess
import os
import json

# Goes to a url in start url array and fetches all the menu items and prices. stores these in 
# the global variable sC. These values are returned by the values function. This function should be
# called by the other python script for each url.
# Takes the url from the user as argument of the values function and returns the corresponding menu

sC=[]
itemj, pricej, desj = [], [], []

class MenuSpider(scrapy.Spider):
    name = "menu2"
    # start_urls = [
    #     'https://www.foodpanda.pk/restaurant/s2ao/second-cup-coffee-company-gulberg'
    # ]
    start_urls = []
    def __init__(self, x):
        self.start_urls = [x]

    def parse(self, response):
        x=response.css('div.menu__items ul.dish-list')
        for i in range(0,(len(x)-1)):
            it = x[i]
            for item in it.css('li'):
                itemj.append(item.css("h3 span::text").extract_first().strip())
                pricej.append(item.css("footer span::text").extract_first().strip())
                desj.append(item.css("p::text").extract_first())
        global sC
        sC = [{"Item": t, "Price": s, "Desc": d} for t, s, d in zip(itemj, pricej, desj)]
        # print sC

def values(url):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'result.json',
        'LOG_ENABLED' : False
    })

    process.crawl(MenuSpider, x=url)
    process.start() 
    # print sC
    return sC 
   
    # print x   

# https://api.paitoo.com.pk/restaurants/all
# https://api.paitoo.com.pk/restaurants/restaurant/5ab51d5f62013e000f885c13
# final version