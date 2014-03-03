# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:58:09 2014

@author: pratool
"""

"""
You have a certain number of clicks (say 10), to get from one Wikipedia page to
another (from all results) from just the hyperlinks on that page within Wikipedia.

OR

You have to trace a path between two different Wikipedia articles.
"""

from pattern.web import *
import math
import pickle
from collections import Counter
 
import re
from itertools import izip

w = Wikipedia()

def wikipage(the_text):
    reverse_text=the_text[::-1]
    if reverse_text.find("secnerefeR") != -1:
        reference_location=reverse_text.index("secnerefeR")
        reverse_text=reverse_text[reference_location+10:len(reverse_text)]
    text=reverse_text[::-1]
    flist=re.split('\W+',text)
    c=0
    l=len(flist)
    while c<=l-1:
        if len(flist[c])<=7: #looks for words less than 4 characters.
            del flist[c]
            l=l-1
            c = c-1
        c +=1
    for n in range(len(flist)-1):
        flist[n]=str(flist[n])
        if flist[n].find("\xe2\x80\x93") != -1:
            del flist[n]
             
    cnt = Counter()
    for word in flist:
        cnt[word] += 1
    return cnt

def dot_product(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

def cosine_measure(v1, v2):
    prod = dot_product(v1, v2)
    len1 = math.sqrt(dot_product(v1, v1))
    len2 = math.sqrt(dot_product(v2, v2))
    return prod / (len1 * len2)

def compare_wiki(dic1,dic2):
    list1=[]
    list2=[]
    
    mega2=dic2
    for word in dic1:
        if word not in dic2:
            mega2[word]=0
    
    mega1=mega2.copy()
    for key in mega1:
        key1=key
        if key1 in dic1:
            mega1[key1]= dic1[key1]
        else:
            mega1[key1]=0
    
    for key in mega1:
        list1.append(mega1[key])
    for key in mega2:
        list2.append(mega2[key])
    
    sim=cosine_measure(list1,list2)
    return sim

#print compare_wiki({'blue':2, 'red':2,'purple':2, },{'purple':2,'red':2, 'blue':2})
#us = wikipage(w.search('United States').plaintext())
#basil = wikipage(w.search('Philip McRae').plaintext())
#print compare_wiki(wikipage(w.search('United States').plaintext()),wikipage(w.search('List of countries by military expenditures').plaintext()))   
#print compare_wiki(wikipage(w.search('Basil McRae').plaintext()),wikipage(w.search('Philip McRae').plaintext()))
#print compare_wiki(basil, basil)

def wikipage_unittest():
    x=wikipage('1blue 1blue red 12345')
    print 'input:', "('1blue 1blue red 12345')"
    print 'expected output:', '1blue:2 12345:1'
    print 'actual output:', x
    print ""
    x=wikipage('(8*1blue) 8blue vlue red')
    print 'input:', "(8*1blue) 8blue vlue red'"
    print 'expected output:' ,'1blue:1 8blue:1 vlue:1'
    print 'actual output:' , x
    print ""
    x=wikipage('2010-2011 [born in 2008]')
    print 'input:', '2010-2011 [born in 2008]'
    print 'expected output:' ,'2010:1 2011:1 born:1 2008:1'
    print 'actual output:' , x
    print ""
    x=wikipage('8*2/twenty')
    print 'input:', '8*2/twenty'
    print 'expected output:' ,'twenty:1'
    print 'actual output:' , x
    print ""
    x=wikipage('[122] blue-blue*blue[blue]blue')
    print 'input:', '[122] blue-blue*blue[blue]blue'
    print 'expected output:' ,'blue:5'
    print 'actual output:' , x
    print ""
    x=wikipage('red blue References redd References hello')
    print 'input:', "red blue References hello"
    print 'expected output:' ,'blue:1 References:1 redd:1'
    print 'actual output:' , x
    print ""

def reverse_articles(article1, article2):
    """
    This checks if the title of an article that is linked from one wikipedia page
    can be accessed from that wikipedia page. This can be slow, esp. if they don't.
    Returns 1 if the articles can link to each other. Returns 0 if they can't.
    """
    for links1 in article1.links:
        if links1 == article2.title:
            for links2 in article2.links:
                if links2 == article1.title:
                    return True
    return False

def find_next_article_forward(article, target_article):
    """
    This function finds the best article to look at after the current article
    by comparing the linked wikipedia pages of the article to the target article.
    """
    global w
    text_init = article.links
    text_targ = get_link_freq(target_article.links)
    all_links = []
    
    for link in article.links:
        if link == target_article.title:
            return target_article
    
    for i in range(len(text_init)-1):
        all_links.append(get_link_freq(w.search(text_init[i]).links))
#        print i, 'of', len(text_init)  # Displays progress of hyperlink parsing
    
    for i in range(len(text_init)-2):
        avg1 = (links_analysis(text_targ, all_links[i]) + compare_wiki(text_targ, all_links[i])) / 2.0
        avg2 = (links_analysis(text_targ, all_links[i+1]) + compare_wiki(text_targ, all_links[i+1])) / 2.0
        if avg1 > avg2:
            article_name = text_init[i]
    
    return w.search(article_name)
        
def links_analysis(target_links, links2):
    """
    This analyzes the hyperlinked wikipedia articles in the target page (target_links)
    and the links provided as a second argument. For every similar term, the raw
    comparison value is increased by 1. This returns the raw comparison value divided
    by the maximum number of links they could have in common (all of the links in
    target links).
    """
    global w
    
    num_same = 0
    
    for title in target_links:
        if title in links2:
            num_same = num_same + 1;
    
    return num_same / float(len(target_links))

def get_link_freq(links):
    """
    This function finds the frequency of each hyperlink (from the links argument)
    and stores the hyperlinked article title as the key to the dictionary hyperlinks
    and the frequency of each link as the value of each key.
    """
    hyperlinks = {}
    
    for the_links in links:
        if the_links in hyperlinks:
            hyperlinks[the_links] = hyperlinks[the_links] + 1
        else:
            hyperlinks[the_links] = 1
    
    return hyperlinks

def get_article_path(article, target_article, path):
    """
    Find the next article along the path of between 2 articles by analyzing the
    similarity between the a hyperlinked article from one page to that page and
    the target page.
    """
    if article == target_article:
        path.append(str(article.title))
    else:
        next_article = find_next_article_forward(article, target_article)
        path.append(str(article.title))
        get_article_path(next_article, target_article, path)
        return path

# UNIT TESTS
    
def reverse_articles_UT():
    philip = w.search('Philip McRae')
    ice = w.search('Ice hockey')
    basil = w.search('Basil McRae')
    
    print reverse_articles(basil, philip)   # Returns True
    print reverse_articles(philip, basil)   # Returns True
    print reverse_articles(ice, philip)     # Returns False
    print reverse_articles(philip, ice)     # Returns False

def get_link_freq_UT():
    aegean_article = get_link_freq(w.search('Aegean Sea'))
    fifa_article = get_link_freq(w.search('FIFA World Cup'))
    
    print aegean_article
    print fifa_article

def links_analysis_UT():
    ireland_article = get_link_freq(w.search('Ireland'))
    uk_article = get_link_freq(w.search('United Kingdom'))
    nepal_article = get_link_freq(w.search('Nepal'))
    
    print links_analysis(ireland_article.links, uk_article.links)
    print links_analysis(ireland_article.links, nepal_article.links)
    print links_analysis(ireland_article.links, ireland_article.links)
 
def find_next_article_forward_UT():
    philip = w.search('Philip McRae')
    ice = w.search('Ice hockey')
    
    print find_next_article_forward(philip, ice)
    
    ireland = w.search('Ireland')
    uk = w.search('United Kingdom')
    
    print find_next_article_forward(ireland, uk)
    
    basil = w.search('Basil McRae')
    jih = w.search('Junior ice hockey')
    tml = w.search('Toronto Maple Leafs')
    
    print find_next_article_forward(basil, jih)
    print find_next_article_forward(tml, jih)
    
def get_article_path_UT():
    basil = w.search('Basil McRae')
    ice = w.search('Ice hockey')
    nyr = w.search('New York Rangers')
    
    print get_article_path(basil, ice, [])
    print get_article_path(basil, nyr, [])
    
get_article_path_UT()
find_next_article_forward_UT()