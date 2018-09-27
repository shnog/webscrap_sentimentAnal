"""This module demonstrates consuming an RSS feed with python
"""
import csv
import feedparser
from bs4 import BeautifulSoup

reuters_rss_url = "http://feeds.reuters.com/reuters/businessNews"
feed = feedparser.parse(reuters_rss_url)
idx = 0
how_many_to_print = 1
fieldnames = ['title', 'summary']
csv_filename = 'rss_feed_out.csv'
with open(csv_filename, mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for post in feed.entries:
        title = post.title
        short_description = post.summary
        clean_short_description = BeautifulSoup(short_description, "lxml").text
        writer.writerow({'title': title, 'summary': clean_short_description})
        if idx < how_many_to_print:
            print(f"Title: {title}")
            print(f"Summary: {clean_short_description}")
        idx += 1
