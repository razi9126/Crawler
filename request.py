import requests
import sys
import subprocess
import menu2
# prints the records which have the foodpandaUrl field.
# Now need to alter menu.py so that it takes this url as a commandline argument. then
# returns the json object array to this program. This program would then iterate over all the fields 
# Calls the values function of menu2.py for each url. Menu is the array of json objects. Each
# object is a menu item.

r = requests.get("https://api.paitoo.com.pk/restaurants/all")
data = r.json()
url = 'https://api.paitoo.com.pk/restaurants/newMenuItem'
for rest in data:
	if 'foodpandaUrl' in rest:
		# print rest['foodpandaUrl']
		# print rest
		menu =menu2.values(rest['foodpandaUrl'])
		for item in menu:
			print item
			newurl= url + '/'+ rest['_id']
			sent = requests.post(newurl, data=item)
			print(sent.status_code, sent.reason)
