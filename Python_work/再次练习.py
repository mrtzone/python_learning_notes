#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:23:33 2019

@author: tianmengxu
"""

importer='\n请输入您的年龄，以此判断收费标准'
importer += "\n在您输入年龄完毕后，请输入'退出'以退出程序："
while True:
    age=input(importer)
    if age == '退出':
        break
    age = int(age)
    if age <= 3:
        print('您的年龄为：'+str(age)+'岁，免费')
    elif age <=12:
        print('您的年龄为：'+str(age)+'岁，收费10元')
    elif age <= 100:
        print('您的年龄为：'+str(age)+'岁，收费15元')
    else:
        print('您的年龄超出范围，请重新输入')
print('finished！！')