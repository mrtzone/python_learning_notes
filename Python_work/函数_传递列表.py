#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:02:48 2019

@author: tianmengxu
"""



def print_models(place_storage,now_place):
    
    while place_storage:
        extract = place_storage.pop()
        print('打印过程:'+extract.title())
        now_place.append(extract)
def show_now_place(now_place):
    print('这些零部件打印好了')
    for place in now_place:
        print(place.title())
place_storage=['robot','phone','person']
now_place=[]
print_models(place_storage[:],now_place)
show_now_place(now_place)
print(place_storage)
    