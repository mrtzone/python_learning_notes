#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:48:35 2019

@author: tianmengxu
"""

输入=('请输入您的年龄：')
输入 += ("输入年龄结束后，请输入'退出'退出程序")
while True:
    message = input(输入)
    if message=='退出':
        break
    message=int(message)
    if message < 4:
        print('您的年龄为'+str(message)+'岁,免费的哦')
    elif message < 13:
        print('您的年龄为'+str(message)+'岁，收费10元')
    elif message < 120:
        print('您的年龄为'+str(message)+'岁，收费15元')
    elif message >120:
        print('无效，请重新输入')
    elif message=='退出':
        break
    