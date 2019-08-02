#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:51:07 2019

@author: tianmengxu
"""

import unittest
from job11_3 import Employee

class TestEmployee(unittest.TestCase):
    '''测试模块Employee'''
    def setUp(self):
        """创建一组员工的个人信息"""
        self.jin = Employee('zhao','jin', 65000)
        
    def test_give_default_raise(self):
        '''测试使用默认年薪增加值是否可行'''
        self.jin.give_raise()
        self.assertEqual(self.jin.wage, 70000)
        
    def test_give_custom_raise(self):
        '''测试自定义年薪增加量是否可行'''
        self.jin.give_raise(10000)
        self.assertEqual(self.jin.wage, 75000)
        
unittest.main()
        