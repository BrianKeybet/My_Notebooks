# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 00:09:42 2022

@author: support.user2
"""

import itertools

list_of_lists = [[1,3,4], [4,8], [3,9,0]]
flat_lists = list(itertools.chain(*list_of_lists))

print(flat_lists)