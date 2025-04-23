# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:30:40 2025

@author: nuraliyev
"""

#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
#Lug'atdagi har bir kalit va qiymatni for sikli yordamida, alifbo ketma-ketligida
#chiqoryli qilib konsolga chiqaring.

python_lugat = {'variable' : 'Ma\'lumotlarni saqlash uchun joy',
                'function' : 'Qayta ishlatiladigan kodlar to\'plami',
                'loop' : 'Kodni bir necha marta bajarish imkonini beradi',
                'list' : 'Bir necha qiymatlarni saqlaydi',
                'tuple' : 'O\'zgarmas qiymatlar ketma-ketligi',
                'dictionary' : 'Kalit-qiymat juftligini saqlaydi',
                'class' : 'Yangi turdagi obyektlar yaratish uchun ishlatiladi',
                'exception' : 'Xatolik holatlarini tutish va boshqarish uchun ishlatiladi',
                'modul' : 'Tashqi fayl yoki kutubxona',
                'import' : 'Boshqa modul yoki kutubxonalarni dasturga qo\'shish'}

print("Python izohli lug'ati:")
for kalit, izoh in python_lugat.items():
    kalit = kalit.capitalize()
    izoh = izoh.lower()
    
    print(f"\n {kalit} bu {izoh}")
    