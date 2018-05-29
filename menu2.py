import scrapy
from scrapy.crawler import CrawlerProcess
import os
import json
sC=[]

itemj, pricej, desj = [], [], []
class MenuSpider(scrapy.Spider):
    name = "menu2"
    start_urls = [
        'https://www.foodpanda.pk/restaurant/s2ao/second-cup-coffee-company-gulberg'
    ]

    def parse(self, response):
        place =response.css("h1.fn::text").extract_first().strip()
        for it in response.css('div.menu__items ul.dish-list'):
            for item in it.css('li'):
                # yield{
                #     'item': item.css("h3 span::text").extract_first().strip(),
                #     'price': item.css("footer span::text").extract_first().strip(),
                #     'description': item.css("p::text").extract_first()
                # }
                itemj.append(item.css("h3 span::text").extract_first().strip())
                pricej.append(item.css("footer span::text").extract_first().strip())
                desj.append(item.css("p::text").extract_first())

        sC = [{"Item": t, "Price": s, "Desc": d} for t, s, d in zip(itemj, pricej, desj)]
        # print json.dumps(sc)
        print sC


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

process.crawl(MenuSpider)
process.start()           
print sC

# https://api.paitoo.com.pk/restaurants/all
# https://api.paitoo.com.pk/restaurants/restaurant/5ab51d5f62013e000f885c13
