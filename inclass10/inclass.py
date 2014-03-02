# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:04:08 2014

@author: pratool
"""

f = open('pg174.txt', 'r')
full_text = f.read()
f.close()

def clean_up(the_text):
    
print full_text.index(" ***")