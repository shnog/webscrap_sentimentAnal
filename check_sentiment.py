import nltk
from typing import List, Tuple, NewType
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rss_feed import get_rss_feed, get_matching_articles, ArticleInfo

nltk.download('vader_lexicon')
#inspired from https://opensourceforu.com/2016/12/analysing-sentiments-nltk/
feed_output_filename = 'rss_feed_out.csv'
result = get_rss_feed()
articles: List[ArticleInfo] = get_matching_articles(result)
#print(articles)
sid = SentimentIntensityAnalyzer()
#these type hints are not needed but make it clearer
SentimentScore = NewType('SentimentScore', float)
ArticleTitle = NewType('ArticleTitle', str)
#scored_articles: List[Tuple[ArticleInfo, SentimentScore]] = []
scored_article_titles: List[Tuple[ArticleTitle, SentimentScore]] = []
for article_info in articles:
    title = ArticleTitle(article_info.title)
    #summary = article_info.summary
    ss = sid.polarity_scores(title)
    compound_score = ss['compound']
    score = SentimentScore(compound_score)
    scored_tuple = (title, score)
    scored_article_titles.append(scored_tuple)
    #print all scores
    # for k in ss:
    #     print(f"{k}: {ss[k]}, ", end='')
    # print()


#lambda sorts by second key, sentiment score
scored_article_titles.sort(key=lambda x : x[1], reverse=False)
print(scored_article_titles)
