#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:37:28 2019

@author: tianmengxu
"""

class Employee():
    '''这是一个表示雇员的类'''
    def __init__(self,first_name,last_name,wage):
        '''初始化雇员'''
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage
        
    def give_raise(self,amount=5000):
        '''给雇员加薪'''
        self.wage += amount
        
        
        
    