#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:41:47 2019

@author: tianmengxu
"""

unconfirmed_users = ['alice','james','tomas']
confirmed_users=[]
while unconfirmed_users:
    
    current_user=unconfirmed_users.pop()
    print('核实后的用户为：'+current_user.title())
    confirmed_users.append(current_user)
print('\n所有已经验证的用户为：')
for user in confirmed_users:
    print(user.title())