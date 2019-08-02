#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:48:37 2019

@author: tianmengxu
"""

def show_magicians(now_name,great_name):
    while now_name:
        extract_name = now_name.pop()
        great_name.append(extract_name)
def make_greak(great_name):
    print('他们都是了不起的魔术师：')
    for name in great_name:
        print('the Great' + ' ' + name.title())
now_name=['zhangsan','lisi','wanger']
great_name=[]
show_magicians(now_name,great_name)
make_greak(great_name)