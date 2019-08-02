#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:55:29 2019

@author: tianmengxu
"""

import json

number = [2,3,4,5,6]
filename = '/Users/tianmengxu/Desktop/Python_work/文件数据/number.json'
with open(filename,'w') as file_object:
    json.dump(number,file_object)