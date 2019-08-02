#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:19:28 2019

@author: tianmengxu
"""

responses = {}
polling_active = True
while polling_active:
    name = input('\n你的名字：')
    response=input('\n你对于这个问题的看法：')
    responses[name] = response
    print(responses)
    repeat = input('你会把这个调查告诉给其他人吗？(是/否)')
    if repeat == '否':
        polling_active = False
print('\n---调查结束---')
for name,response in responses.items():
    print(name+'你喜欢'+response+'.')