#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:18:12 2019

@author: tianmengxu
"""

from 筛子 import Die

d10 = Die(sides=10)
result3 = []
for num in range(10):
    result = d10.roll_die()
    result3.append(result)
print(result3)


