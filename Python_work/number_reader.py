#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:04:09 2019

@author: tianmengxu
"""

import json

filename = '/Users/tianmengxu/Desktop/Python_work/文件数据/number.json'
with open(filename) as file_objeck:
    number = json.load(file_objeck)
print(number)