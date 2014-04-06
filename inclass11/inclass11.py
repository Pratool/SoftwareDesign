# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 15:58:10 2014

@author: Pratool Gadtaula
"""
import math

class Point(object):
    """ Represents a point in 2D space """

origin = Point()

origin.x = 0
origin.y = 0

some_point = Point()
some_point.x = 3
some_point.y = 4

print p_dist(some_point, origin)

def p_dist(point1, point2):
    return math.sqrt((point1.x-point2.x)**2 +(point1.y-point2.y)**2)

class Time(object):
    """ Represends time in hh:mm:ss """

def time_disp(time):
    print str(time.hour)+':'+str(time.minute)+':'+str(time.second)

def increment(time, seconds):
    time.second += (seconds % 60)
    time.minute += int(seconds / 60) % 60
    time.hour += int(seconds / (60**2))

time = Time()
time.hour = 4
time.minute = 38
time.second = 0

time_disp(time)
increment(time, 300)
time_disp(time)