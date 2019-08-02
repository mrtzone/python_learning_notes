#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:38:09 2019

@author: tianmengxu
"""

def make_pizza(size,*toppings):
    print('\n顾客点了' + str(size) + '寸的披萨，配料分别是：')
    for pizza in toppings:
        print(pizza)
make_pizza(12,'lolo','da','das')
make_pizza(10,'popo')
