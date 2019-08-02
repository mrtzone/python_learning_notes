#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:42:08 2019

@author: tianmengxu
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''
    
    def test_first_last_name(self):
        '''测试能够正确的处理像Zhao Jin这样的姓名吗?'''
        formatted_name = get_formatted_name('zhao','jin')
        self.assertEqual(formatted_name,'Zhao Jin')
    
    def test_first_last_middle(self):
        '''能够正确的处理像Zhao Yao Jin这样的姓名吗？'''
        formatted_name = get_formatted_name('zhao','jin','yao')
        self.assertEqual(formatted_name,'Zhao Yao Jin')
        
        
        
unittest.main()