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
import pickle

w = Wikipedia()

def pickling_wiki():
    """
    This allows us to save the data of an individual website. However, Wikipedia
    does not have search limits like Google/Bing/Yahoo so it's not necessary. I
    also realized that by pickling data, you must reduce the data structure from
    Wikipedia type to a generic string. That flattening of information makes it
    more difficult to search in one swoop.
    """
    w = Wikipedia()
    
    ireland_article = w.search('Ireland')
    
    ireland_links = ireland_article.links
    
    f = open('ireland.pickle', w)
    
    for items in ireland_links:
        pickle.dump(items + '\n')
    
    f.close()

def reverse_articles(article1, article2_title):
    """
    This checks if the title of an article that is linked from one wikipedia page
    can be accessed from that wikipedia page. This can be slow, esp. if they don't.
    """
    for links1 in article1.links:
        if links1 == article2_title:
            return 1
    
    return 0

def get_next_path(article, target_article):
    """
    Text analysis part. This might be better if further broken down.
    
    TODO:
    Find the next article along the path of between 2 articles by analyzing the
    similarity between the a hyperlinked article from one page to that page and
    the target page.
    """
    


ireland_article = w.search('Ireland')
uk_article = w.search('United Kingdom')
nepal_article = w.search('Nepal')

print reverse_articles(ireland_article, uk_article.title)   # Returns 1 because they do link to each other
#print reverse_articles(ireland_article, nepal_article.title)   # Returns 0 because they don't link to each other