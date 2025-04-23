# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:05:59 2025

@author: nuraliyev
"""
#Quyidagi oz'garuvchilarning (street, village, district, region) qiymatini foydalanuvchidan
#so'rang. Va avvalgi mashqni takrorlang.

street = input("Ko'changizning nomini kiriting: ")
village = input("Mahallangizning nomini kiriting: ")
district = input("Tumaningnizning nomini kiriting: ")
region = input("Viloyatingizning nomini kiriting: ")

#Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan
#o'zgaruvchiga yuklang

manzil = f"{street} ko'chasi,\n{village} mahallasi,\n{district} tumani,\n{region} viloyati"

#manzil ga biz o'rgangan title(), upper(), lower(), capitalize() metodlarini qo'llab ko'ring.

print(manzil.title())

