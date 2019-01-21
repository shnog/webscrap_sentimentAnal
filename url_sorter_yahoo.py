# URL Sorter Yahoo
#  - Takes all weblinks for articles on the front page of Yahoo Finanace
#      and puts them in a list
#
# Inputs:
# Outputs: Links (lists)

import re
import requests
from bs4 import BeautifulSoup as soup

#url = 'https://finance.yahoo.com/'
#url_str = 'https://finance.yahoo.com'
#req = requests.get(url)
#page_html = req.content
#page_soup = soup(page_html, "html.parser")
#links = page_soup.findAll('a', attrs={'href':re.compile("^/news/")})

def URL_Sorter_Yahoo():
    url = 'https://finance.yahoo.com/'
    url_str = 'https://finance.yahoo.com'
    req = requests.get(url)
    page_html = req.content
    page_soup = soup(page_html, "html.parser")
    links = page_soup.findAll('a', attrs={'href':re.compile("^/news/")})
    addresses = []
    for link in links:
        address = link.get('href')
        address = url_str + address
        addresses.append(address)
    return addresses
