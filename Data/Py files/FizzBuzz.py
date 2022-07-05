# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:48:15 2022

@author: support.user2
"""

posts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,30]

for post in posts:
    #if post % 3 == 0 and post % 5 == 0:
    if post % 15 == 0:
        print(f"{post} FizzBuzz")
    elif post % 3 == 0:
        print(f"{post} Fizz")
    elif post % 5 == 0:
        print(f"{post} Buzz")
    else:
        print(post)