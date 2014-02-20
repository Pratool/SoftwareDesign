# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Pratool Gadtaula
"""

from random import randint
import math
import Image

def build_random_function(min_depth, max_depth):
    """ Builds a random function using fundamental sine, cosine, and product
        functions. The function runs from the maximum depth to the minimum depth,
        therefore having a net depth of the difference between the maximum and
        minimum depths.
    """
    
    # base case can terminate this function because x and y do not need any other
    # arguments
    if (max_depth == min_depth):
        funcs = ['x', 'y']
        return funcs[ randint(0, (len(funcs)-1)) ]
    else:
        functions = ['prod', 'cos_pi', 'sin_pi', 'cosh', 'sinh']
        rand_num = randint(0, len(functions)-1)
        if rand_num == 0:
            return [functions[rand_num], build_random_function(min_depth, max_depth-1), build_random_function(0, max_depth-1)]
        elif rand_num >= 1:
            return [functions[rand_num], build_random_function(min_depth, max_depth-1)]

def evaluate_random_function(f, x, y):
    """ Evaluates the random function built previously recursively by putting in the values
        of x and y in the base case. This function calls itself until it can reach
        this case.
    """
    if f[0] == 'cos_pi':
        return math.cos( math.pi*evaluate_random_function(f[1], x, y ) )
    elif f[0] == 'sin_pi':    
        return math.sin( math.pi*evaluate_random_function(f[1], x, y ) )
    # modified versions of hyperbolic sine and cosine so that all values
    # input between -1 and 1 have an output between -1 and 1
    elif f[0] == 'cosh':
        return ( (2*math.e)/(1+math.e**2) )*math.cosh( evaluate_random_function(f[1], x, y) )
    elif f[0] == 'sinh':
        return ( (2*math.e)/(1-math.e**2) )*math.sinh( evaluate_random_function(f[1], x, y) )
    elif f[0] == 'prod':
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    elif f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y

def save_random_pictures(name):
    """ Evaluates random functions generated from above amd maps their values
        onto red, green, and blue channels of a bitmap with a width and height
        of 350 pixels. Saves this bitmap with
        the name input to the function.
    """
    
    red_chan = build_random_function(2, 8)
    blue_chan = build_random_function(2, 8)
    green_chan = build_random_function(2, 8)
    
    width = 350
    height = 350
    
    im = Image.new("RGB", (width, height))
    
    for i in range(width):
        for j in range(height):
            # maps the i and j values to x and y so that x and y are between
            # the range of -1 and 1
            x_val = 2*(i+1)/350.0 - 1
            y_val = 2*(j+1)/350.0 - 1
            
            # maps the output of each red, green, blue channel functions from
            # [-1, 1] to [0, 255]
            # NOTE: color values must be integers
            r = int(( evaluate_random_function(red_chan, x_val, y_val) + 1 ) * 255.0 / 2)
            b = int(( evaluate_random_function(blue_chan, x_val, y_val) + 1 ) * 255.0 / 2)
            g = int(( evaluate_random_function(green_chan, x_val, y_val) + 1 ) * 255.0 / 2)
            
            im.putpixel( [i,j], (r,g,b) )
    
    im.save(name + ".bmp")

for i in range(11):
    save_random_pictures('tests' + str(i))
