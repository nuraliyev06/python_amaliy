# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:14:43 2025

@author: nuraliyev
"""
#foydalanuvchilar degan ro'yxat tuzing, unga kamida 5 ta login qo'shing.
#Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
#foydalanuvchilar ro'yxatining tarkibi bilan solishtiring. Agar ro'yxatda
#bunday login mavjud bo'lsa, "Login band, yangi login tanlang!", aks xolda
#"Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

xabar = "Login band, yangi login tanlang!"

foydalanuvchilar = ['fashagaming', 'nuraliyev', 'cobalt_tuning', 'eat_food', 'drluntik']

foydalanuvchi = input("Yangi login tanlang: ")

if foydalanuvchi in foydalanuvchilar:
    print(xabar)
else:
    print(f"Xush kelibsiz, {foydalanuvchi}!")
    


