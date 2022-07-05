# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:20:45 2022

@author: support.user2
"""
numbers = [2,13,12,2,57,45,13,78,90,8,10,8]
num_without_dup = set(numbers)
num_list = []

for num in numbers:
    if num in num_without_dup:
        num_list.append(num)
        
print(num_list)