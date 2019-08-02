#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:38:23 2019

@author: tianmengxu
"""
import json
favorite_number = input('请输入你最喜欢的数字:')

file_number = 'favorite_number.json'
with open(file_number,'w') as file_object:
    json.dump(favorite_number,file_object)
    