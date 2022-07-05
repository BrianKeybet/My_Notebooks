# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:24:48 2022

@author: support.user2
"""

numbers = [42, 73, 0, 16, 10]
odds = []
evens = []
for num in numbers:
    #Returns false for even numbers
    if num % 2:
        odds.append(num)
    else:    
        evens.append(num)
        
print("Even numbers:" , evens)
print(f'Odd numbers: {odds}')

#list comprehension
odds= [num for num in numbers if num % 2]        

print(odds)