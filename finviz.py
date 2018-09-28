"""Downloads articles from finviz"""
import re
import csv
import os.path
import sys
import requests
from bs4 import BeautifulSoup as soup
def download_finviz_articles(should_cache_html_file=True):
    """Downloads finviz news and
    saves a list of titles and links to a CSV file

    If should_cache_html_file is True then checks if temp.html exists
    If it does exist then use that as html file to parse, otherwise download copy
    If should_cache_html_file is False then redownload html file each time
    """
    my_url = 'https://finviz.com/news.ashx'

    #Environment Variables to set run configurations

    #if True saves response to a file and queries that instead of the web page
    html_tmp_cache_filename = "temp.html"

    #makes excel file and writes approiate headers
    csv_filename = "articles.csv"
    fieldnames = ['title', 'URL']

    def get_page_html_soup(url: str):
        """Retrieves html from url and creates a soup out of it"""
        req = requests.get(url)
        page_html = req.content
        page_soup = soup(page_html, "html.parser")
        return page_soup


    #Acquire html for page. If should_cache_html_file is True then cache results.
    page_soup = None
    if should_cache_html_file:
        #if cache file does not exist then create it
        if not os.path.isfile(html_tmp_cache_filename):
            with open(html_tmp_cache_filename, 'wb') as temp_file:
                req = requests.get(my_url)
                temp_file.write(req.content)
        #read from cache file
        try:
            with open(html_tmp_cache_filename, 'rb') as temp_file:
                page_html = temp_file.read()
                page_soup = soup(page_html, "html.parser")
        except FileNotFoundError as fnfe:
            print(fnfe)
            sys.exit(1)
    else:
        #if not cacheing file, load page_soup same way as before
        page_soup = get_page_html_soup(my_url)

    #finds all clickable links as an item
    links = page_soup.findAll("tr", {"class":"nn"})

    #first item in links list
    #testlink1 = links[0]

    #title of item (blog/article)
    #title = testlink1.a.text

    #url from the clickable link of item
    #weblink = testlink1.a['href']

    #puts all links found on webpage into a array
    newlinks = []
    i = 0
    #using with here to open the file will automatically close it at the end
    with open(csv_filename, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for link in page_soup.findAll('a', attrs={'href':re.compile("^http://")}):
            article_url = link.get('href')
            newlinks.append(article_url)
            #takes away the u in front of the url string for better format
            article_title = links[i].a.text
            #writes url and title to the csv file
            writer.writerow({'title': article_title, 'URL' : article_url})
            i += 1


if __name__ == '__main__':
	download_finviz_articles()
