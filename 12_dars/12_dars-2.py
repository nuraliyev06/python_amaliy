# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:38:35 2025

@author: nuraliyev
"""
#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
#keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

davlatlar = {'aqsh' : 'Washington',
             'italiya' : 'Rim',
             'malayziya' : 'Kuala-Lumpur',
             "o'zbekiston" : 'Toshkent',
             'qirg\'iziston' : 'Bishkek',
             "qozog'iston" : 'Dushanbe',
             'rossiya' : 'Moskva',
             'singapur' : 'Singapur',
             'tojikiston' : 'Nursulton'}

#print("Davlatlarning nomi:")

#for davlat in sorted(davlatlar):
#    print(davlat.upper())
    
#print("\nDavlatlarning poytaxtlari:")

#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.upper())

#Foydalanuvchidan istalgan davlatni kiritishini so'rang va shu davlatning poytaxtini
#konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
#"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlat = input("Qaysi davlatning poytaxtini bilmoqchisiz: ").lower()

if davlat not in davlatlar:
    print("Bizda bu davlat haqida ma'lumot yo'q.")
else:
    if davlat == 'aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    
    print(f"{davlat}ning poytaxti {davlatlar[davlat.lower()]} shahri hisoblanadi.")