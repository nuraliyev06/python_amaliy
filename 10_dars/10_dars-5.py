# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:42:06 2025

@author: nuraliyev
"""
#10_dars-4 amaliy topshiriqda bajarilgan dasturni quyidagicha o'zgartiring.
#Foydalanuvchidan 5 ta mahsulot kiritishini so'rang. Foydalanuvchi so'ragan va
#do'konda bor mahsulotlarni yangi bor_mahsulotlar degan ro'yxatga,
#do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
#Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor"
#degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ...
#degan xabarni chiqaring.


mahsulotlar = ['un', 'shakar', 'tuxum', 'sut', 'choy', 'yog\'', 'non', 'kartoshka', 'piyoz', 
               "go'sht"]

savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas =[]

for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot.capitalize())
    else:
        mavjud_emas.append(mahsulot.capitalize())

if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
else:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)

        