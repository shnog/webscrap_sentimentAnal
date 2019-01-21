# URL to Article
#  - Extracts the Yahoo Finance article from the URL and converts it into a string
#
# Inputs: link (str)
# Outputs: article (str)

import requests
from bs4 import BeautifulSoup as soup

def URL_to_Article(link):
    url = link # different for each site
    req = requests.get(url)
    page_html = req.content
    page_soup = soup(page_html, "html.parser")
    article = ""
    content = page_soup.findAll("p", {"type":"text"})
    try:
        for paragraph in content:
            #print(paragraph.text)
            article = article + paragraph.text + " "
    except AttributeError:
        print("Sam is a faggot")
        pass
    return article

