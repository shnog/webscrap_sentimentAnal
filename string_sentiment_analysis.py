# String Reader
#  - Takes text in string form and gives a sentiment analysis score
#
# Inputs: arcticle (str)
# Outputs: core (float)

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

def String_Reader(article):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(article) # can only analysis strings
    score = ss['compound']
    return float(score)
