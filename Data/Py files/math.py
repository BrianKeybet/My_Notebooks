# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:32:27 2022

@author: support.user2
"""
#Calculates circumfirence for an angle of 12 degrees
from math import radians, pi

r = 192500

dist = r * radians(12)

print(dist)

dist2 = pi * 2*192500 * 12/360

print(dist2)