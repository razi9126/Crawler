import requests

# prints the records which have the foodpandaUrl field.
# Now need to alter menu.py so that it takes this url as a commandline argument. then
# returns the json object array to this program. This program would then iterate over all the fields 
# //
r = requests.get("https://api.paitoo.com.pk/restaurants/all")
data = r.json()

for i in data:
	if 'foodpandaUrl' in i:
		print i['foodpandaUrl']