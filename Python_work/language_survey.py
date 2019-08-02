#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:52:29 2019

@author: tianmengxu
"""

from survey import AnonynousSurvey

question = '你最喜欢哪门编程语言'
my_survey = AnonynousSurvey(question)

my_survey.show_question()
print('请输入‘退出’以退出程序')
while True:
    response = input('输入编程语言:')
    if response == '退出':
        break
    my_survey.store_response(response)
    
print('\n谢谢您参与我们的调查')
my_survey.show_results()