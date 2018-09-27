"""This module demonstrates consuming an RSS feed with python
"""
import csv
import sys
import feedparser
from bs4 import BeautifulSoup

reuters_rss_url = "http://feeds.reuters.com/reuters/businessNews"
feed = feedparser.parse(reuters_rss_url)
idx = 0
how_many_to_print = 1
fieldnames = ['title', 'summary']
csv_filename = 'rss_feed_out.csv'
#create a set of titles from the rss
titles = set()
with open(csv_filename, mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for post in feed.entries:
        title = post.title
        titles.add(title)
        short_description = post.summary
        clean_short_description = BeautifulSoup(short_description, "lxml").text
        writer.writerow({'title': title, 'summary': clean_short_description})
        if idx < how_many_to_print:
            print(f"Title: {title}")
            print(f"Clean summary: {clean_short_description}")
            print(f"Messy summary: {short_description}")
        idx += 1

matched_titles = []
finviz_results_filename = 'articles.csv'
try:
    with open(finviz_results_filename, mode='r') as article_file:
        article_reader = csv.reader(article_file, delimiter='\t')
        for row in article_reader:
            title = row[0]
            #check if finviz title was in RSS feed
            if title in titles:
                matched_titles.append(title)
except FileNotFoundError as fnfe:
    #TODO: handle this by calling TEST_RUN.py
    #to call it TEST_RUN should export it's functions as module
    print()
    print(f"Could not find {finviz_results_filename}")
    print("Try running script TEST_RUN.py")
    sys.exit(1) # triggers exit as error

print()
print(f"Matched Titles: {matched_titles}")
