# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:09:58 2014

@author: pratool
"""

import random

def is_between(x, y, z):
    if y >= x and y <= z:
        return True
    
    return False


def random_float(start, stop):
    return random.random()*(stop - start) + start
    
def factorial_func(n):
    x = 1
    if n == 0:
        return 1
    else:
        for i in range(n-1):
            x = x*(n+1)
        return x


#print random_float(5, 14)
print factorial_func(3)