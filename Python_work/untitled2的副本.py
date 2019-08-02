#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 21:01:37 2019

@author: tianmengxu
"""

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://hotel.qunar.com/")
data = driver.title
print (data)
