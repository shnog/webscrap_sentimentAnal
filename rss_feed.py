"""This module demonstrates consuming an RSS feed with python
"""
import csv
import os.path
import sys
import feedparser
from bs4 import BeautifulSoup
from finviz import download_finviz_articles
from typing import NamedTuple, List
from collections import namedtuple

ArticleInfo = namedtuple('ArticleInfo',['title','summary'])

def get_rss_feed(
    rss_feed_url='http://feeds.reuters.com/reuters/businessNews'
    )-> List[ArticleInfo]:
    """Retrieves content of reuters rss url
    Downloads finviz news titles if it does not exist
    Prints article titles found on both reuters rss and finviz"""

    feed = feedparser.parse(rss_feed_url)
    article_infos : List[ArticleInfo] = []

    for post in feed.entries:
        title = post.title
        short_description = post.summary
        clean_short_description = BeautifulSoup(short_description, "lxml").text
        article_infos.append(ArticleInfo(title,clean_short_description))
    return article_infos

def get_matching_articles(rss_feed_article_info_list : List[ArticleInfo],
    finviz_results_filename = 'articles.csv') -> List[ArticleInfo]:
    matched_articles: List[ArticleInfo] = []

    if not os.path.isfile(finviz_results_filename):
        download_finviz_articles(should_cache_html_file=False)
    try:
        with open(finviz_results_filename, mode='r') as article_file:
            article_reader = csv.reader(article_file, delimiter='\t')
            for row in article_reader:
                finviz_title = row[0]
                #check if finviz title was in RSS feed
                for article_info in rss_feed_article_info_list:
                    rss_feed_title = article_info.title
                    if finviz_title == rss_feed_title:
                        matched_articles.append(article_info)
    except FileNotFoundError as fnfe:
        print(fnfe)
        sys.exit(1) # triggers exit as error

    return matched_articles

def save_rss_feed(output_filename='rss_feed_out.csv'):
    """Retrieves content of reuters rss url
    Downloads finviz news titles if it does not exist
    Prints article titles found on both reuters rss and finviz"""

    fieldnames = ['title', 'summary']
    with open(output_filename, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for article_info in get_rss_feed():
            writer.writerow({'title': article_info.title, 'summary': article_info.summary})


if __name__ == '__main__':
    save_rss_feed()
