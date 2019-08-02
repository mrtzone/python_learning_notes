#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:48:01 2019

@author: tianmengxu
"""

#car
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条支出汽车总里程的信息"""
        print("这辆汽车已经跑了" + str(self.odometer_reading) + "公里")
        
    def update_odometer(self,mileage):
            """将里程表读数设定为指定的值
            禁止将里程数回调
            """
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print('不能回调里程数')
                
    def increment_odometer(self,miles):
        """讲里程表读数增加到指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('禁止往回拨')

class ElectricCar(Car):
    """电动车的独特之处"""
    
    def __init__(self, make, model, year):
        """电动车的独特之处
        初始化父类属性，再初始化电动车特有的属性
        """
        
        super().__init__(make, model, year)
        self.battery_size = 70

    def descriptive_battery(self):
        """答应一条描述电量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_besla = ElectricCar('tesla', 'model s', 2016)
print(my_besla.get_descriptive_name())
my_besla.descriptive_battery()
            
my_used_car = Car('audi','a4',2013)
print('\n'+my_used_car.get_descriptive_name())

my_used_car.update_odometer(360000)
my_used_car.read_odometer()

my_used_car.increment_odometer(6000)
my_used_car.read_odometer()

