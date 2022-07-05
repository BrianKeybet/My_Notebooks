# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:48:54 2022

@author: support.user2
"""
numbers = [2,13,12,57,45,78,90,10,8]

#Long Way
max = numbers[0]
for number in numbers:
    if number > max:
        max = number      
print(max)

#Easy way
#x = max(numbers)
#print(x)