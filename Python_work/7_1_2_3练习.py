#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:43:58 2019

@author: tianmengxu
"""

car=input('你想要租什么车:')
print('好的，你选择的【'+car+'】马上给你寄过来')
person=input('请问有点少人用餐：')
person=int(person)
if person > 8:
    print('抱歉，没有空桌了')
else:
    print('请用餐')
Integer_multiple=input('Please enter a number to determine if it is an integer multiple of 10：')
Integer_multiple=int(Integer_multiple)
if Integer_multiple % 10 != 0:
    print('This number '+'['+str(Integer_multiple)+']'+' Not an integer of 10')
else:
    print('This number '+'['+str(Integer_multiple)+']'+' Is an integer of 10')
    