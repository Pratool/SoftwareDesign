# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:33:22 2014

@author: pratool
"""
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
 
bob.pen_color = 'red'

bob.delay = .01

def my_regular_polygon(lower_left, side_len, num_sides):
    bob.x = lower_left[0]
    bob.y = lower_left[1]
    
    for i in range(num_sides):
        bob.fd(side_len)
        bob.lt(360.0/num_sides)
    
    wait_for_user()

def my_square(lower_left, side_len):
    my_regular_polygon(lower_left, side_len, 4)

def my_circle(center, radius):
    side_len = math.pi*radius/60.0
    my_regular_polygon([center[0]-side_len, center[1]-radius], side_len, 120)
    
def snow_flake_side(l, level):
    """ Draw a side of the snowflake curve with side length l and recursion
        depth of level
    """
    if level == 1:
        bob.fd(l)
        bob.rt(60)
        bob.fd(l)
        bob.lt(120)
        bob.fd(l)
        bob.rt(60)
        bob.fd(l)
    else:
        snow_flake_side((l/3.0), level-1)
        bob.rt(60)
        snow_flake_side((l/3.0), level-1)
        bob.lt(120)
        snow_flake_side((l/3.0), level-1)
        bob.rt(60)
        snow_flake_side((l/3.0), level-1)

def snow_flake(l, level):
    for i in range(3):
        snow_flake_side(l, level)
        bob.lt(120)

def sierp_triangle(l, level, coord):
    if level == 1:
        fd(l)
        lt(120)
        fd(l)
        lt
    else:
        sierp_triangle

snow_flake(50, 5)
wait_for_user()