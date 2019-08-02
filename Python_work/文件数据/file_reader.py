#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:59:52 2019

@author: tianmengxu
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())