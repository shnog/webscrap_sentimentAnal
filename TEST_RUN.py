import time
import requests
import re
import csv
import os.path
import sys

from urllib.parse import urlsplit


my_url = 'https://finviz.com/news.ashx'

#Environment Variables to set run configurations

#if True saves response to a file and queries that instead of the web page
should_cache_file = True
html_tmp_cache_filename = "temp.html"



#makes excel file and writes approiate headers
csv_filename = "articles.csv"
fieldnames = ['title','URL']


#soup code that works on most websites but not on finviz
#uClient = uReq(my_url)
#page_html = uClient.read()
#uClient.close()

def get_page_html_soup(url: str):
	req = requests.get(url)
	page_html = req.content
	page_soup = soup(page_html,"html.parser")
	return page_soup


#Acquire html for page. If should_cache_file is True then cache results.

page_soup = None
if should_cache_file:
	#if cache file does not exist then create it
	if not os.path.isfile(html_tmp_cache_filename):
		with open(html_tmp_cache_filename,'wb') as temp_file:
			req = requests.get(my_url)
			temp_file.write(req.content)
	#read from cache file
	try:
		with open(html_tmp_cache_filename,'rb') as temp_file:
			page_html = temp_file.read()
			page_soup = soup(page_html, "html.parser")
	except FileNotFoundError as fnfe:
		print(fnfe)
		sys.exit(1)
else:
	#if not cacheing file, load page_soup same way as before
	page_soup = get_page_html_soup(my_url)

#finds all clickable links as an item
links = page_soup.findAll("tr",{"class":"nn"})

#first item in links list
#testlink1 = links[0]

#title of item (blog/article)
#title = testlink1.a.text

#url from the clickable link of item
#weblink = testlink1.a['href']

#puts all links found on webpage into a array
i = 0
newlinks = []

#using with here to open the file will automatically close it at the end
with open(csv_filename, mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter='\t')
	writer.writeheader()
	for link in page_soup.findAll('a',attrs={'href':re.compile("^http://")}):
		newlinks.append(link.get('href'))
		article_url = newlinks[i]
		article_title = links[i].a.text
		#writes url and title to the csv file
		writer.writerow({'title': article_title, 'URL' : article_url})
		i = i + 1

urls = {}
for link in newlinks:
	#req = requests.get(link)
	#base_url = "{0.netloc}/".format(urlsplit(link))
	base_url = f"{urlsplit(link).netloc}"
	if base_url in urls:
		urls[base_url] += 1
	else:
		urls[base_url] = 1

#Prints how many of each link there are

#list comprehension
#inspired from https://stackoverflow.com/questions/11228812/print-a-dict-sorted-by-values
d_view = [ (v,k) for k,v in urls.items() ]
d_view.sort(reverse=True) # natively sort tuples by first element
for v,k in d_view:
    print(f"{k}: {v}")
#A majority of the links actually go to feedproxy.google.com
#we need to traverse those links and see where they actually point
