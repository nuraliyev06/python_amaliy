# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:09:17 2025

@author: nuraliyev
"""
#Foydalanuvchidan bugun nechta odam bilan uchrashganini so'rang, va har bir suhbatlashgan
#odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

odam_soni = int(input("Bugun nechta odam bilan suhbatlashdingiz: "))
odamlar = []
for n in range(odam_soni):
    odamlar.append(input(f"{n+1}-suhbatlashgan odamingiz kim edi: "))

print(odamlar)