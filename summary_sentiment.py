import re
import csv
import os.path
import sys
import requests
from bs4 import BeautifulSoup as soup
from typing import List
from collections import namedtuple
import feedparser
import nltk
from typing import List, Tuple, NewType
from nltk.sentiment.vader import SentimentIntensityAnalyzer


csv_filename = "summaryscore.csv"
fieldnames = ['title', 'URL', 'summary','score']

url = 'https://finviz.com/news.ashx?v=2'
req = requests.get(url)
page_html = req.content
page_soup = soup(page_html, "html.parser")

newlinks = []
links = page_soup.findAll("tr", {"class":"nn"})
i = 0

with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for link in page_soup.findAll('a', attrs={'href':re.compile("^http://")}):
            # Gets title and URL
            article_url = link.get('href')
            newlinks.append(article_url)
            article_title = links[i].a.text
            # Gets summary
            summary = links[i]
            summarydata = summary.contents[3]
            summarydatatitle = summarydata['title']
            datasum = summarydatatitle.split('>')[3]
            datasum = datasum.split('<')[0]
            # Gets sentiment of summary
            sid = SentimentIntensityAnalyzer()
            ss = sid.polarity_scores(datasum)
            compound_score = ss['compound']
            #writes url, title, summary and score to the csv file
            writer.writerow({'title' : article_title, 'URL' : article_url, 'summary' : datasum, 'score' : compound_score})
            i += 1

