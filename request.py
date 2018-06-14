import requests
import sys
import subprocess
import crawling
import time
# This program iterates over all restaurants
# Checks whether a restaurant has the foodpandaurl field or not. If it has then,
# Calls the values function of menu2.py for each url. Menu is the array of json objects. Each
# object is a menu item.
# Sends the post request for each menu item to the api for that particular restaurant id
# Should output (200,OK) for all individual menu items

# --MOHAMMAD RAZI UL HAQ--

r = requests.get("https://api.paitoo.com.pk/restaurants/all")
data = r.json()
url = 'https://api.paitoo.com.pk/restaurants/newMenuItem'
for rest in data:
	if 'foodpandaUrl' in rest:
		if "foodpanda" in rest['foodpandaUrl']:
			if "http" in rest['foodpandaUrl']:
				print rest['foodpandaUrl']
				import c
				# if (rest['foodpandaUrl'])!= undefined
				try:
					menu =crawling.values(rest['foodpandaUrl'])
					# time.sleep(5)
					for item in menu:
						newurl= url + '/'+ rest['_id']
						print item
						# sent = requests.post(newurl, data=item)
						# print(sent.status_code, sent.reason)
					time.sleep(3)
				except Exception as err:
					print("Erro {}".format(err))
			else:
				print ("https://" + rest['foodpandaUrl'])
				try:
					menu =crawling.values("https://" + rest['foodpandaUrl'])
					# time.sleep(5)
					for item in menu:
						newurl= url + '/'+ rest['_id']
						print item
						# sent = requests.post(newurl, data=item)
						# print(sent.status_code, sent.reason)
					time.sleep(3)
				except Exception as err:
					print("Erro {}".format(err))