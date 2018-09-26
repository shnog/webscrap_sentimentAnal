import time
import requests
import re
from bs4 import BeautifulSoup as soup

my_url = 'https://finviz.com/news.ashx'

#makes excel file and writes approiate headers
filename = "articles.csv"
f = open(filename,"w")
headers = "title, URL\n"
f.write(headers)

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
for link in page_soup.findAll('a',attrs={'href':re.compile("^http://")}):
	newlinks.append(link.get('href'))
	#takes away the u in front of the url string for better format
	article_url = newlinks[i].encode("utf-8")
	article_title = links[i].a.text
	#writes url and title to the csv file
	f.write(article_title + "," + str(article_url) + "\n")

	i = i + 1

f.close()

#takes the u in front of the url out on the first link
#newlinks[0].encode("utf-8")
