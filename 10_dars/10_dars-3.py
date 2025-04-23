# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:26:11 2025

@author: nuraliyev
"""
#Foydalanuvchidan ikkita son kiritishini so'rang, sonlarni solishtiring va
#ularning teng yoki katta/kichikligi haqida xabarni chiqaring.

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    print(f"{son1} = {son2}")
elif son1 < son2:
    print(f"{son1} < {son2}")
else:
    print(f"{son1} > {son2}")
    
