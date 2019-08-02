#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:14:49 2019

@author: tianmengxu
"""

def show_magicians(list_names,great_list_names):
    while list_names:
        extract_name = list_names.pop()
        great_list_names.append(extract_name)
def make_greak(great_list_names):
    print('\n升级的魔术师:')
    for great_name in great_list_names:
        print('the Great' + ' ' + great_name.title())
list_names=['zhaojin','yangzhangliu','suisui']
great_list_names=[]
show_magicians(list_names[:],great_list_names)
make_greak(great_list_names)
print('原来的列表为：')
print(list_names)
    
        
    
        