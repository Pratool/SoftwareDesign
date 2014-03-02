# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:00:26 2014

@author: Pratool Gadtaula
"""

def reverse_lookup(value, input_dict):
    rev_dict = []
    for keys in input_dict:
        if input_dict[keys] == value:
            rev_dict.append(keys)
    return rev_dict

my_dict = {'hey':'salut', 'informal greeting':'salut', 'hello':'bonjour'}
print reverse_lookup('salut', my_dict)
print my_dict