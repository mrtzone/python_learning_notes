#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:32:51 2019

@author: tianmengxu
"""
from random import randint


class Die():
    """创建一个骰子随机数"""
    def __init__(self,sides):
        self.sides = sides
        
    
    def roll_die(self):
        return randint(1,self.sides)
    
d6 = Die(sides=8)
print(d6.roll_die())


        
        
        
    