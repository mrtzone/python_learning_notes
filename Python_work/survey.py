#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:37:13 2019

@author: tianmengxu
"""

class AnonynousSurvey():
    """收集匿名调查问卷"""
    
    def __init__(self,question):
        """存储一个问题，并未存储答案做准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
        
    def store_response(self,new_response):
        """存储单份调查答案"""
        self.responses.append(new_response)
        
    def show_results(self):
        """显示已经收集的答案"""
        print('问题答案为:')
        for response in self.responses:
            print('-' + response)