#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:18:25 2019

@author: tianmengxu
"""

import json

def get_greet_user():
    '''如果存储了用户名，就获取它'''
    filename = 'usernames166.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_user():
    '''提示用户输入用户名'''
    username = input('请输入用户名：')
    filename = 'usernames166.json'
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
    return username
    
        

def greet_user():
    '''问候用户的名字，并指出其姓名'''
    username = get_greet_user()
    if username:
        content = input('你输入的用户名为：' + username + '请输入‘是’或‘否’来确认用户名:')
        if content == '是':
            print('欢迎回来，' + username + '!')
        elif content == '否':
            username = get_new_user()
            print('我们会记住你的姓名，欢迎你下次回来' + username + '!')
    else:
        username = get_new_user()
        print('我们会记住你的姓名，欢迎你下次回来' + username + '!')
        

greet_user()
