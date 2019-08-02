#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:09:49 2019

@author: tianmengxu
"""
file = '/Users/tianmengxu/Desktop/PYTHON编程从入门到实践/《Python编程》源代码文件/chapter_10/pi_million_digits.txt'
with open(file) as file_objeck:
    lines = file_objeck.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input('请输入你的生日，格式是mmddyy:')
if birthday in pi_string:
    print('你的生日在π里面呢')
else:
    print('很抱歉，你的生日不在这里面')