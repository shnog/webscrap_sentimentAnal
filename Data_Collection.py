# Data Collection
#  - Collections data (score,article,date,URL) from Yahoo Finance site and logs into a CSV file
#
# Inputs:
# Outputs: 

from yahoo_reader import URL_to_Article
from string_sentiment_analysis import String_Reader
from url_sorter_yahoo import URL_Sorter_Yahoo
from Article_to_CSV import Article_to_CSV

def data_collection():
    print("Collection...")
    addresses = URL_Sorter_Yahoo() # Yahoo Finance front page weblink addresses
    for link in addresses:
        article = URL_to_Article(link) # 1
        score = String_Reader(article) # 2
        filename = Article_to_CSV(link,article,score) # 3
    print("Done with Collection")

#link = "https://finance.yahoo.com/news/recent-study-validates-operational-effectiveness-120100006.html"
#article = URL_to_Article(link) # 1
#score = String_Reader(article) # 2
#filename = Article_to_CSV(link,article,score) # 3