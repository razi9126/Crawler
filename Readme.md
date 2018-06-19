README

Mohammad Razi Ul Haq

Only "crawling.py" and "request.py" needed to extract menus and post each menu item for each
restaurant to its addMenuItem api call. Currently the post lines are commented and 
instead the items are being printed to the screen only. Uncomment the post lines in
request.py to make the program actually send POST requests.

menu2.py used scrapy library to scrape however it did not support twisted reactor restarting
needed to fetch each individual webpage on each call of the values function.