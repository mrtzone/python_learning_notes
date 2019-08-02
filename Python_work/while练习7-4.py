#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:06:18 2019

@author: tianmengxu
"""

提示='\n请输入披萨配料'
提示 += "\n当您在输入'结束'后停止输入"
message=''
while message != '结束':
    message = input(提示)
    if message == '结束':
        print('点餐完毕，谢谢！！！')
    else:
        print('我们会在此披萨中添加此配料')