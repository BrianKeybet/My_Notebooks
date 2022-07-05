# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:31:53 2022

@author: support.user2
"""
numbers = [2,13,12,2,57,45,13,78,90,8,10,8]
seen = set()
dupes = []

for num in numbers:
    if num in seen:
        dupes.append(num)
    else:
        seen.add(num)
        
print(dupes)
print(seen)