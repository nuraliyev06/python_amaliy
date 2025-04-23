# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:01:04 2025

@author: nuraliyev
"""
#Python izohli lug'ati tuzing. :ug'atga kamida 10 ta atamani kiriting va har
#birining qisqacha tarjimasini yozing.

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

#Foydalanuvchidan biror so'z kiritishini so'rang va so'zning tarjimasini chiqarib
#bering. Agar so'z lug'atda mavjud bo'lmasa, "Bunday so'z lug'atda mavjud emas"
#degan xabarni chiqaring.

kalit = input("Kalit so'zni kiriting: ").lower()
#print(python_lugat.get(kalit, "Bunday so'z lug'atda mavjud emas"))

#Yuqoridagi vazifani if-else yordamida bajaring va natijani ham foydalanuvchiga
#tushunarli ko'rinishda chiqaring.

if kalit not in python_lugat:
    print("Bunday so'z lug'atda mavjud emas.")
else:
    print(f"{kalit.capitalize()} bu {python_lugat[kalit].lower()}")