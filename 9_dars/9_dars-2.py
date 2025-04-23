# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:34:43 2025

@author: nuraliyev
"""
#Foydalanuvchi ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
#Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring
#Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

user = input("Ismingizni kiriting: ")

if user.lower() == "admin":
    print(f"Xush kelibsiz {user.capitalize()}.")
    print("Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {user.capitalize()}!")
