#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:52:39 2019

@author: tianmengxu
"""
import tesserocr
from PIL import Image
image = Image.open('/Users/tianmengxu/Desktop/image.txt')
print(tesserocr.image_to_text(image))