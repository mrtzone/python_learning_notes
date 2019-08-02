#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:03:20 2019

@author: tianmengxu
"""

def make_shirt(size,word='I LOVE PYTHON'):
    """打印尺码及字样在T恤上"""
    print('此T恤的尺码为：'+size)
    print('此T恤的字样为：'+word)
make_shirt('大号','宋体')
make_shirt(word='黑体',size='中号')
make_shirt(size='大大号')
def describe_city(city,country="China"):
    print(city.title()+" belong to "+country.title())
describe_city('guiyang')
describe_city(country="USA",city='new york')
describe_city(city="shenzheng")
    
