#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:02:09 2019

@author: tianmengxu
"""

unconfirmed_users = ['alice','james','tomas']
confirmed_users=[]
while unconfirmed_users:
    for users in unconfirmed_users:
        po=unconfirmed_users.pop()
        confirmed_users.append(po)
print(confirmed_users)