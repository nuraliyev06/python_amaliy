# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:14:46 2025

@author: nuraliyev
"""
#Foydalanuvchidan juft son kiritishini so'rang. Agar foydalanuvchi juft son kiritsa
#"Rahmat!", agar toq son kiritsa "Bu juft son emas!" degan xabarni chiqaring.

son = float(input("Juft son kiriting: "))

if son%2 == 0:
    print("Rahmat!")
else:
    print("Bu juft son emas!")
