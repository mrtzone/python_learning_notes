#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:53:08 2019

@author: tianmengxu
"""
dream_place={}
name_input='请输入您的姓名:'
place_input='请输入您想去的地点：'
end_input="需不需要把此问答交给您的朋友(需要/不需要)"

dream_active=True
while dream_active:
    name=input(name_input)
    place=input(place_input)
    dream_place[name]=place
    end=input(end_input)
    if end == '不需要':
        dream_active=False
    for name,place in dream_place.items():
        print(name+'你最想去的地方是：'+place)
    