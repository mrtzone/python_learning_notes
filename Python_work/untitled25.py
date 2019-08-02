#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:19:34 2019

@author: tianmengxu
"""

import unittest
from job11_3 import Employee

class TestEmployee(unittest.TestCase):
    """测试Employee类"""
    
    def setUp(self):
        """初始化一个员工"""
        self.zhaojin = Employee('zhao','jin', 60000)
        
    def test_give_deault_raise(self):
        '''测试默认初始工资是否相加'''
        self.zhaojin.give_raise()
        self.assertEqual(self.zhaojin.wage, 65000)
        
    def test_rasult_raise(self):
        '''测试自定义的初始工资是否相加'''
        self.zhaojin.give_raise(10000)
        self.assertEqual(self.zhaojin.wage, 70000)
         
unittest.main()