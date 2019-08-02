#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:17:20 2019

@author: tianmengxu
"""

import unittest
from cc11_1 import c_place
class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        """能够正确的处理像'Guiyang China'这样的地名吗?"""
        formatted_place = c_place('guiyang','china')
        self.assertEqual(formatted_place,'Guiyang China')
    
    def test_city_country_person_numbers(self):
        """能够正确的处理像'Guiyang China 800000'这样的地名吗？"""
        formatted_place = c_place('guiyang','china',800000)
        self.assertEqual(formatted_place,"Guiyang China 800000")
        

unittest.main()


