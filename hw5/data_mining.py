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

counter = 0

def get_path(article, target_article, path):
    """
    Text analysis part. This might be better if further broken down.
    
    **NOTE: Already being further broken down**
    
    TODO:
    Find the next article along the path of between 2 articles by analyzing the
    similarity between the a hyperlinked article from one page to that page and
    the target page.
    """
    global w
    global counter
    if counter < 5:
        print counter
        if reverse_articles(article, target_article.title) == 1:
            return [article.title, target_article.title]
        else:
            counter = counter + 1
            if counter == 1:
                path.append(article.links[6]);
                get_path(w.search(article.links[6]), target_article, path)
            if article.links[6] == path[len(path)-1]:
                path.append(article.links[7])
                get_path(w.search(article.links[7]), target_article, path)
            else:
                path.append(article.links[6]);
                get_path(w.search(article.links[6]), target_article, path)
    
    return path
#    return 'Too long'
#    return 'Could not find direct link'

def find_next_article(article, target_article):
    global w;
    text_init = article.links
    text_targ = get_link_freq(target_article.links)
    all_links = []
    
    for link in text_init:
        all_links.append(get_link_freq(w.search(link).links))
        print link
    
    for i in len(range(all_links)):
        print i
        if links_analysis(text_targ, all_links[i]) > links_analysis(text_targ, all_links[i+1]):
            article_name = text_init[i]
    
    return article_name;
        
def links_analysis(target_links, links2):
    global w
    
    num_same = 0
    
#    target_links = get_link_freq(target_links)
#    links2 = get_link_freq(links2)
    
    for title in target_links:
        if title in links2:
            num_same = num_same + 1;
    
    return num_same / float(len(target_links))

def get_link_freq(links):
    hyperlinks = {}
    
    for the_links in links:
        if the_links in hyperlinks:
            hyperlinks[the_links] = hyperlinks[the_links] + 1
        else:
            hyperlinks[the_links] = 1
    
    return hyperlinks
    
def shorter_dict(dict1, dict2):
    if (len(dict1) <= len(dict2)):
        return [dict1, dict2]
    return [dict2, dict1]

#ireland_article = w.search('Ireland')
#uk_article = w.search('United Kingdom')
#nepal_article = w.search('Nepal')
#aegean_article = w.search('Aegean Sea')
#fifa_article = w.search('FIFA World Cup')

tudor = w.search('Tudor conquest of Ireland')
plant = w.search('Plantation of Ulster')

#print links_analysis(ireland_article.links, uk_article.links)
#print links_analysis(ireland_article.links, nepal_article.links)
#print links_analysis(ireland_article.links, ireland_article.links)

print find_next_article(tudor, plant)

#print reverse_articles(ireland_article, uk_article.title)   # Returns 1 because they do link to each other
#print reverse_articles(ireland_article, nepal_article.title)   # Returns 0 because they don't link to each other

#print get_path(ireland_article, nepal_article, [])

#print get_next_path(ireland_article, uk_article)
#print get_next_path(ireland_article, nepal_article)