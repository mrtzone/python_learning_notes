#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:09:21 2019

@author: tianmengxu
"""

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
    
class Battery():
    def __init__(self,battery_size=70,car_model='s'):
        
    
        
        self.battery_size = battery_size
        self.car_model = car_model
           
        
    def describe_battery(self):
        print('这辆车有' + str(self.battery_size) + '-KWH battery')
          
    def get_range(self):
        """打印一条消息，支出电瓶的续航里程"""
        sss
        if self.battery_size == 70 and self.car_model == 's':
            range = 240
        elif self.battery_size == 85 and self.car_model == 'a':
            range = 270
        else:
            range = '?'
        
        message = '这辆电动车可以跑' + str(range)
        message = message + '公里'
        print(message)
        
class ElectricCar(Car):
    

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    

my_besla = ElectricCar('tesla', 'model s', 2016)
print(my_besla.get_descriptive_name())
my_besla.battery.describe_battery()
my_besla.battery.get_range()



