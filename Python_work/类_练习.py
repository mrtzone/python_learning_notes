#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:19:02 2019

@author: tianmengxu
"""

class User():
    def __init__(self,first_name,last_name,user_age,user_hight,greetings='您好'):
        self.f_name=first_name
        self.l_name=last_name
        self.age=user_age
        self.hight=user_hight
    def describe_restaurant(self):
        print('你姓：'+self.f_name.title())
        print('你名：'+self.l_name.title())
        print('你的年龄'+str(self.age))
        print('你的身高为:'+str(self.hight))
    def greet_user(self):
        print(self.greetings.title()+'欢迎您的到来')
users_1=User('das','fd',56,56)
users_1.describe_restaurant()
