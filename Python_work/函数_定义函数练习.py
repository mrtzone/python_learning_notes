#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:26:50 2019

@author: tianmengxu
"""
def display_message():
    """PYTHON函数"""
    print('我在本章学习了函数的形参和实参，并用于调用它')
display_message()
def favorite_book(bookname):
    """写出你喜欢的数据"""
    print('你最喜欢的书籍是:'+bookname.title())
favorite_book('shiwangeweihsa')