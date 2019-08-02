# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+' is now sitting')
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+' now rolled over!')

my_dog=Dog('huanhuan',6)
print("我的小狗名字是:"+my_dog.name.title())
print('小狗今年'+str(my_dog.age)+'岁')
my_dog2=Dog('dada',9)
my_dog2.sit()
my_dog2.roll_over()

my_dog3=Dog('lala',12)
your_dog=Dog('zaza',10)

print('我的狗叫：'+my_dog3.name.title()+'.')
print('我的小狗今年:'+str(my_dog3.age)+'岁')
my_dog3.roll_over()

print('你的的狗叫：'+your_dog.name.title()+'.')
print('你的小狗今年:'+str(your_dog.age)+'岁')
your_dog.roll_over()       


