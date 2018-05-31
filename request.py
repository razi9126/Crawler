import requests
import sys
import subprocess
import menu2

# This program iterates over all restaurants
# Checks whether a restaurant has the foodpandaurl field or not. If it has then,
# Calls the values function of menu2.py for each url. Menu is the array of json objects. Each
# object is a menu item.
# Sends the post request for each menu item to the api for that particular restaurant id

r = requests.get("https://api.paitoo.com.pk/restaurants/all")
data = r.json()
url = 'https://api.paitoo.com.pk/restaurants/newMenuItem'
for rest in data:
	if 'foodpandaUrl' in rest:
		menu =menu2.values(rest['foodpandaUrl'])
		for item in menu:
			# print item
			newurl= url + '/'+ rest['_id']
			sent = requests.post(newurl, data=item)
			print(sent.status_code, sent.reason)
