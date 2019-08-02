# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

输入值="\n请输入'quit'退出程序!!"
输入值 += '\n若你输入其他内容，那么程序将会一直运行：'
#message = ""
#while message != 'quit':
    #message=input(输入值)
    #if message == '':
        #print(message)
#active=True
#while active:
   # message=input(输入值)
    #if message == 'quit':
       # active=False
    #elif message == 'end':
        #active=False
    #else:
        #print(message)
while True:
    city=input(输入值)
    if city=='quit':
        break
    else:
        print(str(city.title()))
        
    
    
