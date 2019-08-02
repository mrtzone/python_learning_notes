#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:15:16 2019

@author: tianmengxu
"""

filename = '/Users/tianmengxu/Desktop/Python_work/文件数据/guest.txt'
print('请输入批量的用户名,输入‘退出’程序自动退出')
while True:
    
    with open(filename,'a') as file_object:
        guest = input('请输入您的用户名:')
        file_object.write(guest+'\n')
        if guest == '退出':
            break
print('finished!!!!')
    