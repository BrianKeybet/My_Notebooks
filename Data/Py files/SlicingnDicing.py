# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:23:56 2022

@author: support.user2
"""

x = [1,2,3,4,5,6,7,8,9]

print(f"Index 0 to 2:{x[0:3]}")
#Similar to the following
print(f"Index 0 to 2:{x[:3]}")

print(f"Index 1 and 2:{x[1:3]}")

print(f"Index 1 to 2nd last index:{x[6:-1]}")

print(f"Index 6 to last index:{x[6:9]}")
#Similar to the following
print(f"Index 6 to last index:{x[6:]}")

x = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(x[2][0]) 
print(x[2][:2])
print(x[2])
print(x[-1][1]) 