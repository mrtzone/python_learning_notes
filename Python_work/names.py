#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:15:21 2019

@author: tianmengxu
"""

from name_function import get_formatted_name
print('请输入‘退出’，退出程序')
while True:
    first = input('\n请输入姓')
    if first == '退出':
        break
    last = input('请输入名')
    if last == '退出':
        break
    
    name = get_formatted_name(first,last)
    print('\t你的姓名为' + name)