import time
import requests
import re
import csv
from bs4 import BeautifulSoup as soup

my_url = 'https://finviz.com/news.ashx'

#makes excel file and writes approiate headers
csv_filename = "articles.csv"
fieldnames = ['title','URL']


#soup code that works on most websites but not on finviz
#uClient = uReq(my_url)
#page_html = uClient.read()
#uClient.close()

#gets code from url and turns it in a soup
req = requests.get(my_url)
page_html = req.content
page_soup = soup(page_html,"html.parser")

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
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	for link in page_soup.findAll('a',attrs={'href':re.compile("^http://")}):
		newlinks.append(link.get('href'))
		#takes away the u in front of the url string for better format
		article_url = newlinks[i]
		article_title = links[i].a.text
		#writes url and title to the csv file
		writer.writerow({'title': article_title, 'URL' : article_url})
		i = i + 1

#takes the u in front of the url out on the first link
#newlinks[0].encode("utf-8")
