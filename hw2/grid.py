# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:41:55 2014

@author: pratool
"""

def draw_grid():
    draw_top2()
    draw_top2()
    print ('+' + (' - '*4))*2, '+'

def draw_top2():
    print ('+' + (' - '*4))*2, '+'
    print ( ('|' + ' '*12)*2 + '|\n' )*4,

draw_grid()