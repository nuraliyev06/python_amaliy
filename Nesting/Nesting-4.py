# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:53:33 2025

@author: nuraliyev
"""

#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
#ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni 
#konsolga chiqaring.

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

for davlat, malumotlar in davlatlar.items():
   
    davlat = davlat.capitalize()
    poytaxt = malumotlar['poytaxti'].capitalize()
    aholi = malumotlar['aholisi']
    til = malumotlar['tili']
    
    print(f"{davlat}ning poytaxti {poytaxt}\n"
          f"Aholisi: {aholi}\n"
          f"Rasmiy tili: {til.capitalize()}\n")
