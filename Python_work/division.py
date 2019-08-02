#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:47:40 2019

@author: tianmengxu
"""
num = []
print('给我两个有效数字，我会对其做除法输出.')
print('输入‘退出’以退出程序')
while True:
    first_num = input('请输入第一个数字')
    if first_num == '退出':
        break
    second_num = input('请输入第二个数字')
    if second_num == '退出':
        break
   
    try:
        answer = int(first_num)/int(second_num)
    
    except ValueError:
        print('禁止输入字符和0,谢谢!!')   
    except ZeroDivisionError:
        print('禁止输入字符和0,谢谢!!')
    else:
        print(answer)


print("finished!")

