from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib2

sC=[]
itemj, pricej, desj, catj = [], [], [], []

def simple_get(url):
	"""
	Attempts to get the content at `url` by making an HTTP GET request.
	If the content-type of response is some kind of HTML/XML, return the
	text content, otherwise return None.
	"""
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None


def is_good_response(resp):
	"""
	Returns True if the response seems to be HTML, False otherwise.
	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 
			and content_type is not None 
			and content_type.find('html') > -1)


def log_error(e):
	"""
	It is always a good idea to log errors. 
	This function just prints them, but you can
	make it do anything.
	"""
	print(e)

def values(url):
	raw_html = simple_get(url)
	html = BeautifulSoup(raw_html, 'html.parser')
	if len(html)>2:
		categories = html.find_all('div',{'class':'dish-category-header'})

		x = html.find_all('ul',{'class':'dish-list'})				#all the dishes of all categories

		i=0
		while (i < len(x)):
			while (i!=len(x)):

				category = categories[i].text.strip()
				if 'Beverage' in category:
					i=i+1
				elif 'Deal' in category:
					i=i+1
				else:
					break
			
			if (i == len(x)):
				break    
			category=categories[i].text.strip()
			it = x[i]  						#decided the category to expand
			html2 = BeautifulSoup(str(it), 'html.parser')
			for item in html2.find_all('li'):
				html3 = BeautifulSoup(str(item), 'html.parser')
				itemj.append(html3.find('h3',{'class':'dish-name fn p-name'}).text.strip())
				pricej.append(html3.find('span',{'class':'price p-price'}).text.strip())
				catj.append(category)
			
			i=i+1
		global sC
		sC = [{"name": t,"category": c, "price": s,  "shouldClassify": True} for t, c, s in zip(itemj, catj, pricej)]
	else:
		sc=[]
	return sC