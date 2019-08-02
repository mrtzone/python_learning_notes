#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:59:51 2019

@author: tianmengxu
"""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['kala'] = 'python'
favorite_languages['kulua'] = 'c'
favorite_languages['adie'] = 'java'
favorite_languages['kolo'] = 'r'

for name,language in favorite_languages.items():
    print(name.title() + "最喜欢:" + language.title())
    