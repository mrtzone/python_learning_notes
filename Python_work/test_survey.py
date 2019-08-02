#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:06:49 2019

@author: tianmengxu
"""
import unittest
from survey import AnonynousSurvey

class TestAnonynousSurvey(unittest.TestCase):
    """一个针对AnonynousSurvey类的测试"""
    def setUp(self):
        question = '你最喜欢哪一门编程语言?'
        self.my_survy = AnonynousSurvey(question)
        self.responses = ['c','java','c']
    
    
    
    def test_store_single_response(self):
        """测试的单个答案都会被保存下来"""
        self.my_survy.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survy.responses)
        
        
        
        
    def test_store_three_single_response(self):
        """测试的三个答案都会被保存下来"""
        for response in self.responses:
            self.my_survy.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survy.responses)
        
unittest.main()