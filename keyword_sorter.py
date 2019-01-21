# Sorter
# - Takes filename and gives keywords of the article
#
# Input: filename
# Output: keywords

from keywords_finder import article_content, findtags, keywords, company_name
import datetime
filename = 'tesla-gets-green-light-start-000147004.csv'

def keyword_sorter(filename):
    content = article_content(filename)
    keywords(content)
    company = company_name(content)

print("")
now1 = datetime.datetime.now()
print(now1)
print("")
keyword_sorter(filename)
print("")
now2= datetime.datetime.now()
#
print("Time elapsed", now2-now1)