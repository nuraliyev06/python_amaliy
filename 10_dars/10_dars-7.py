# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:21:13 2025

@author: nuraliyev
"""
#Foydalanuvchidan biror butun son kiritishini so'rang. Foydalanuvchi kiritgan
#sonni 2 dan 10 gacha bo'lgan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Butun son kiriting: "))

for n in range(1,11):
    if son%n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")
            

