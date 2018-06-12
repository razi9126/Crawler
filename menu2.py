import scrapy
from scrapy.crawler import CrawlerProcess
import os
import json
import time
import sys
# Goes to a url in start url array and fetches all the menu items and prices. stores these in 
# the global variable sC. These values are returned by the values function. This function should be
# called by the other python script for each url.
# Takes the url from the user as argument of the values function and returns the corresponding menu 
# excluding the items having the words "Deal" or "Beverage" in their category field

# --MOHAMMAD RAZI UL HAQ--

sC=[]
itemj, pricej, desj, catj = [], [], [], []

class MenuSpider(scrapy.Spider):
    name = "menu2"
    start_urls = []
    def __init__(self, x):
        self.start_urls = [x]

    def parse(self, response):
        try:
            x=response.css('div.menu__items ul.dish-list')
            categories = response.css('div.menu__items div.dish-category-header')
            # for i in range(0,(len(x))):
            i=0
            while (i < len(x)):
                while (i!=len(x)):

                    category = categories[i].css("h2.dish-category-title::text").extract_first().strip()
                    if 'Beverages' in category:
                        i=i+1
                    elif 'Deal' in category:
                        i=i+1
                    else:
                        # print i
                        break
                
                if (i == len(x)):
                    break    

                category = categories[i].css("h2.dish-category-title::text").extract_first().strip()
                it = x[i]
                for item in it.css('li'):
                    itemj.append(item.css("h3 span::text").extract_first().strip())
                    # print item.css("h3 span::text").extract_first().strip()
                    pricej.append(item.css("footer span::text").extract_first().strip())
                    # print item.css("footer span::text").extract_first().strip()
                    desj.append(item.css("p::text").extract_first())
                    catj.append(category)
                i=i+1
                global sC
                sC = [{"name": t,"category": c, "price": s, "description": d, "shouldClassify": True} for t, c, s, d in zip(itemj, catj, pricej, desj)]
        except:
            sC=[]

def values(url):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'result.json',
        'LOG_ENABLED' : False
    })

    process.crawl(MenuSpider, x=url)
    process.start() 
    # process.start(stop_after_crawl=False)
    # time.sleep(0.5)
    # os.execl(sys.executable, sys.executable, *sys.argv)
    return sC
    # global sC
    # sC=[] 

# values("https://www.foodpanda.pk/restaurant/s9sn/kfc-johar-town")
# https://api.paitoo.com.pk/restaurants/all
# https://api.paitoo.com.pk/restaurants/restaurant/5ab51d5f62013e000f885c13
# final version