# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:34:38 2014

@author: pratool
"""

def factorialize(n):
    if n == 0:
        return 1
    
    return n*factorialize(n-1)

print factorialize(0)