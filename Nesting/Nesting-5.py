# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 17:59:01 2025

@author: nuraliyev
"""

#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
#lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan 
#xabarni chiqaring.
davlatlar = {
    'yaponiya' : {'poytaxti' : 'tokio',
                  'aholisi' : 125_000_000,
                  'tili' : 'yapon tili',},
    
    'braziliya' : {'poytaxti' : 'braziliya',
                   'aholisi' : 215_000_000,
                   'tili' : 'portugal tili'},
    
    'misr' : {'poytaxti' : 'qohira',
              'aholisi' : 110_000_000,
              'tili' : 'arab tili'},
    
    'shvetsiya' : {'poytaxti' : 'stokgolm',
                   'aholisi' : 10_500_000,
                   'tili' : 'shved tili'}
    }

davlat = input('Qaysi davlat haqida ma\'lumot kerak: ').lower()



error = "Kechirasiz, bizda bu davlat haqida ma'lumot mavjuda emas!"

if davlat not in davlatlar:
    print(error)
else:
    malumotlar = davlatlar[davlat]
    
    poytaxt = malumotlar['poytaxti'].capitalize()
    davlat = davlat.capitalize()
    aholi = malumotlar['aholisi']
    til = malumotlar['tili'].capitalize()
    
    print(f"{davlat}ning poytaxti {poytaxt}\n"
          f"Aholi soni: {aholi}\n"
          f"{davlat}dagi rasmiy til: {til}")