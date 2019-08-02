#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:47:34 2019

@author: tianmengxu
"""

import json

def get_stored_name():
    '''如果用户存储了姓名，就获取它'''        
    file_name = 'favorite_number111.json'
    try:        
        with open(file_name) as file_object:
            your_name = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return your_name
    
def get_new_name():
    '''请输入用户名'''
    u_name = input('请输入用户名:')
    file_name = 'favorite_number111.json'
    with open(file_name,'w') as file_objeck:
        json.dump(u_name,file_objeck)
    return u_name

def greet_you_name():
    '''问候用户，并打印用户名'''
    your_name = get_stored_name()
    if your_name:
        print('欢迎您回来' + your_name)
    else:
        your_name = get_new_name()
        print('欢迎您下次到来' + your_name)

greet_you_name()