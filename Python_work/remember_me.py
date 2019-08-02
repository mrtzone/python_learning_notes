#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:13:52 2019

@author: tianmengxu
"""

import json

username = input('请输入您的姓名:')
filename = 'usernames.json'

with open(filename,'w') as file_objeck:
    json.dump(username,file_objeck)
    print('欢迎回来' + username + '!')