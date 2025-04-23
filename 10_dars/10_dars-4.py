# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:30:27 2025

@author: nuraliyev
"""
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulot kiriting.
#Yangi savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida
#5 ta mahsulot kiritishini so'rang. Savatdagi elementlarni mahsulotlar ro'yxati
#bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor"
#aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ['un', 'shakar', 'tuxum', 'sut', 'choy', 'yog\'', 'non', 'kartoshka', 'piyoz', 
               "go'sht"]

savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        print(f"{mahsulot.capitalize()} do'konimizda mavjud.")
    else:
        print(f"{mahsulot.capitalize()} do'konimizda mavjud emas.")


