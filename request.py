import requests

# prints the record which have the foodpandaUrl field.


r = requests.get("https://api.paitoo.com.pk/restaurants/all")
data = r.json()

for i in data:
	if 'foodpandaUrl' in i:
		print i['foodpandaUrl']