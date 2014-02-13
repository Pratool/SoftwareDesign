# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:41:34 2014

@author: pratool
"""

def cumul_sum(n):
    sum = range(len(n))
    sum[0] = n[0]
    
    for i in range(len(n)-1):
        sum[i+1] = n[i+1]+sum[i]
    
    return sum

print cumul_sum([1,2,3,4])