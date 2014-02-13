# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:40:19 2014

@author: pratool
"""

def get_complementary_base(nucleotide):
    """Takes a base and returns its complement"""
    if (nucleotide == 'A'):
        return 'T'
    elif (nucleotide == 'C'):
        return 'G'
    elif (nucleotide == 'T'):
        return 'A'
    else:
        return 'C'

opposite = get_complementary_base(raw_input('Try a nitrogenous base:\n'))
print opposite