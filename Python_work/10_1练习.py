#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:06:39 2019

@author: tianmengxu
"""

learning_python = '/Users/tianmengxu/Desktop/Python_work/文件数据/至今学到的python.txt'
with open(learning_python) as file_object:
    files = file_object.read()
    files=files.replace('我学习','I LOVE ')
    print(files)
        
    