# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:55:08 2025

@author: nuraliyev
"""
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini
#hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting"
#degan xabarni chiqaring

son = float(input("Musbat son kiriting: "))

if son < 0:
    print("Siz manfiy son kiritdingiz, iltimos musbat son kiriting!")
else:
    print(son**0.5)
