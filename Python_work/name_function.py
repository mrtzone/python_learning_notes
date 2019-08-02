#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:06:00 2019

@author: tianmengxu
"""

def get_formatted_name(first,last,middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    
        
    
    return full_name.title()
    



