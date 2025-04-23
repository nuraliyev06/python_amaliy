# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:56:05 2025

@author: nuraliyev
"""
#Restoran menusi lug'atini tuzing. Foydalanuvchidan 3 ta ovqat buyurtma berishini
#so'rang. Foydalanuvchi kiritgan taomni menu bilan solishtiring. Agar taom menuda bo'lsa
#narhini ko'rsating, aks holda "Bizda bunday taom yo'q" degan xabarni chiqaring.

menyu = {'osh' : 22000,
         'palov' : 22000,
         'manti' : 5000,
         'lag\'mon' : 25000,
         'norin' : 18000,
         'somsa' : 6000,
         'chuchvara' : 20000,
         'qozon kabob' : 40000,
         "do'lma" : 28000,
         'shashlik' : 15000,
         'kompot' : 5000}

print("3 ta taom buyurtma bering.")

buyurtmalar = []

for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taomni kiriting: "))

mavjud_emas = []

for taom in buyurtmalar:
    
    if taom.lower() not in menyu:
        mavjud_emas.append(taom)

if len(mavjud_emas) == 3:
    print("Kechirasiz, siz buyurtma qilgan taomlar bizda mavjud emas.")
    
for taom in buyurtmalar:
    
    if taom.lower() not in menyu and len(mavjud_emas) < 3:
        print(f"Bizda {taom.lower()} mavjud emas.")
        
    elif taom.lower() in menyu:
        print(f"{taom.capitalize()} {menyu[taom.lower()]} so'm.")
    
