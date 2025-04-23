# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:59:46 2025

@author: nuraliyev
"""

#Foydalanuvchidan 5 ta eng seimli kinolarini kiritishini so'rang, va kinolar
#degan ro'yxatga saqlab oling. Natijani konsolga chiqaring

kinolar = []
for n in range(5):
    kinolar.append(input(f"{n+1}-yoqtirgan filmingizning nomini kiriting: "))

print(kinolar)