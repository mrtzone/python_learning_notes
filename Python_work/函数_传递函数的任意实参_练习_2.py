#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:17:58 2019

@author: tianmengxu
"""

def car_message(car_manufacturer,car_model,**other_types):
    car={}
    car['manufacturer']=car_manufacturer
    car['model']=car_model
    for key,value in other_types.items():
        car[key]=value
    return car
make_car=car_message('kangda','A360',color='red',number='12')
print(make_car)
    