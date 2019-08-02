#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:38:52 2019

@author: tianmengxu
"""

sandwich_orders=['tuna sandwich','rice sandwich','pastrami sandwich','pastrami sandwich','pastrami sandwich']
finished_sandwiches=[]
for sandwich in sandwich_orders:
    print('我做好了你的:'+sandwich)
while sandwich_orders:
    laji_sandwiches=sandwich_orders.pop()
    finished_sandwiches.append(laji_sandwiches)
    
for finished_sandwiche in finished_sandwiches:
    print('我做好你的：'+finished_sandwiche)
while 'pastrami sandwich' in finished_sandwiches:
    finished_sandwiches.remove('pastrami sandwich')
print(finished_sandwiches)
                               