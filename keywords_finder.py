# Keyword(s) Finder
#   - Finds high frequency words in the csv article and sorts them onto a new csv file
#
# Inputs: filename (csv)
# Output: summary_data (csv)

import csv
import os
from collections import Counter
import re
import nltk
import urllib.request
import re
import itertools
from fuzzywuzzy import fuzz, process

def article_content(filename):
    path = "/Users/Master Soe/webscrap/Stock Articles/"
    article = path + filename
    lines = [line for line in open(article)]
    try:
        if lines[4] is not "":
            content = lines[4]
            sentiment_score = lines[5]
    except:
        content = lines[2]
        sentiment_score = lines[3]
    #print(content)
    return (content, sentiment_score)

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
    if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

def keywords(content_and_scores):
    content = content_and_scores[0]
    wordtoke = nltk.word_tokenize(content)
    #print(wordtoke)
    wordtag = nltk.pos_tag(wordtoke)
    #print(wordtag)
    nouns = findtags("NN", wordtag)
    verbs = findtags("VB", wordtag)
    adjecs = findtags("JJ", wordtag)
    keyn = []
    print("KEYWORDS FOUND")
    print("")
    print("Nouns")
    for noun in sorted(nouns):
        print(noun, nouns[noun])
        #for p in nouns[noun]:
            #keyn.append(p[0])
    #print(keyn)
    print("")
    print("Verbs")
    for verb in sorted(verbs):
        print(verb, verbs[verb])
    print("")
    print("Ajectives")
    for adjec in sorted(adjecs):
        print(adjec, adjecs[adjec])
    print("")

def company_name(content_and_scores):
    content = content_and_scores[0]
    sentiment = content_and_scores[1]
    wordtoke = nltk.word_tokenize(content)
    wordtag = nltk.pos_tag(wordtoke)
    nouns = findtags("NN", wordtag)
    main_noun = nouns['NNP'][0][0]
    #print(main_noun)

    poscomp = []
    pronouns = nouns['NNP']
    try:
        pronouns_s = nouns['NNPS']
        for pronoun in pronouns:
            #print(pronoun[0])
            poscomp.append(pronoun[0])
        for p in pronouns_s:
            poscomp.append(p[0])
            #print(pronouns)
    except:
        for pronoun in pronouns:
            #print(pronoun[0])
            poscomp.append(pronoun[0])
    #print(poscomp)

    path1 = "/Users/Master Soe/webscrap/Stock Companies/A-Z_companies.csv"
    f = open(path1, newline='')
    reader = csv.reader(f)
    data = [row for row in reader]
    path2 = "/Users/Master Soe/webscrap/Stock Companies/companynames.txt"
    k = open(path2, newline='')
    text = k.read()
    k.close()
    company = poscomp
    badwordlist = ["Corporation", "Co.", "Incorporated", "Inc.", "Company", "Communications" "Fund", "Trust", 
                        "Investment", "Associates", "NYSE", "NASDAQ", "Stock", "Securities", "Bloomberg"]
    #try:
        #for comp in poscomp:
            #if re.search(comp, text):
                #company.append(comp)
                #print(company)
                #raise StopIteration
            #else:
                #pass
                #print("No company found and Sam is faggot")      
    #except StopIteration:
        #pass

    #print(company)
    scores1 = []
    companylist = []
    TICKERlist = []

    # Gets data from data lol
    for companydetails in data:
        #print(companydetails[1])
        companylist.append(companydetails[1])
        TICKERlist.append(companydetails[0])

    # Checks if there are any common words in the list
    for badword in badwordlist:
        for fx in company:
            if re.search(fx,badword):
                company.remove(fx)
            else:
                pass
    # Removes \\ words
    for x in company:
        if re.search('\\\\', x):
            company.remove(x)
        else:
            pass
    for x in company:
        if re.search('\\\\', x):
            company.remove(x)
        else:
            pass
    print("SENTIMENT SCORE", sentiment)
    print("List of possible companies")
    print(company)
    # Makes permutations for the word  
    #for l in data:
    #    companylist.append(l[1])
    #_gen = (itertools.permutations(company, i + 1) for i in range(len(company)))
    #all_permutations_gen = itertools.chain(*_gen)
    #results = [x for x in all_permutations_gen]
    #k = []
    # Arranges the combinations into a readable array
    #for x in results:
    #    j = ""
    #    for y in x:
    #        j = j + y + " "
    #    k.append(j)
    #scores2 = [""]
    #print(k)

    # Checks the match score of word to a company  
    for x in company: 
            #print(x)
        if re.search('[a-z]+', x) is None:
            possible_company_score = process.extract(x, TICKERlist, limit = 3)
        else:
            possible_company_score = process.extract(x, companylist, limit = 3)
            #print(possible_company_score)
            #print(companylistx)
        for x in possible_company_score:
            scores1.append(x)       

    #print(scores1)
    c = Counter(scores1)
    guess_company = c.most_common()
    #print(guess_company)
    i = []
    for g in guess_company:
        i.append(g[0])
    print(" ")  
    def custom_sort(t):
        return t[1]   
    i.sort(key = custom_sort, reverse = True)
    #print(i)
    print("The stock company(s) is", i[0:5])
    #except:
        #pass
                              
    return guess_company
