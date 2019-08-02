#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:05:34 2019

@author: tianmengxu
"""

def get_formatted_name(first_name,last_name):
    """返回简洁的姓名"""
    full_name=first_name+' '+last_name
    return full_name
while True:
    print('\n\n请告诉我你的姓:')
    print("请输入'退出'退出程序")
    f_name=input('first_name:')
    if f_name == '退出':
        break
    print('\n请告诉我你的名:')
    print("请输入'退出'退出程序")
    l_name=input('last_name:')
    if l_name == '退出':
        break
    foemartted_name=get_formatted_name(f_name.title(),l_name.title())
    print('\nHello'+' '+foemartted_name)
print('finished!!')



