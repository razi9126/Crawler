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

for i in data:
	if 'foodpandaUrl' in i:
		# print i['foodpandaUrl']
		menu =menu2.values()
		print menu