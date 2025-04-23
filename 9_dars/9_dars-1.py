# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:17:19 2025

@author: nuraliyev
"""
#Yangi cars = ["toyota", 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat
#elementlarining birinchi harfini katta qilib konsolga chiqaring. GM uchun
#ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car != 'gm':
        print(car.capitalize())
    else:
        print(car.upper())