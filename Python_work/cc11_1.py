#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:11:55 2019

@author: tianmengxu
"""

def c_place(city,country,person_numbers=''):
    if person_numbers:
        full_place = city + ' ' + country + ' ' + str(person_numbers)
    else:
        full_place = city + ' ' + country
    return full_place.title()