# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:01:06 2014

@author: pratool
"""

def check_fermat(a, b, c, n):
    if n >= 2:
        if (a**n + b**n) == c**n:
            print 'Holy smokes, Fermat was wrong!'
        else:
            print 'No, that doesn\'t work.'
    else:
        print 'Try an exponent value greater than 2'

def use_fermat():
    prompt = 'Type in a value for '
    a = int(raw_input(prompt+'a:\n'))
    b = int(raw_input(prompt+'b:\n'))
    c = int(raw_input(prompt+'c:\n'))
    n = int(raw_input(prompt+'n:\n'))
    
    check_fermat(a, b, c, n)

use_fermat()