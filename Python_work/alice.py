#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:22:24 2019

@author: tianmengxu
"""


def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().count('the')
        
        print('这个文件' + filename + '包含' + str(words) + '个单词')
filenames = ['das.txt',
            'uest.txt',
            '/Users/tianmengxu/Desktop/Python_work/文件数据/alice.txt',
            'dsa.txt']
for filename in filenames:
    count_words(filename)