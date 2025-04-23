# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:49:20 2025

@author: nuraliyev
"""
#Foydalanuvchidan istalgan son kiritishini so'rang. Agar son manfiy bo'lsa konsolga
#"Manfiy son", agar musbat "Musbat son" degan xabarni chiqaring.

son = float(input("Istalgan sonni kiriting: "))
if son < 0:
    print("Manfiy son!")
else:
    print("Musbat son!")