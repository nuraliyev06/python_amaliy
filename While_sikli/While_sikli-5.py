# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:47:22 2025

@author: nualiyev
"""
#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
#dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar 
#(mahsulot va uning narhi) kiritishni so'rang.

maxsulotlar = {}

savol = "Maxsulotingizni kiriting"
savol += "(chiqish uchun 'exit' deb yozing): "

while True:
    maxsulot = input(savol)
    if maxsulot.lower() != 'exit':
        narh = input(f"{maxsulot.capitalize()}ning narhini kiriting: ")
        maxsulotlar[maxsulot] = narh
    else:
        break

for maxsulot, narh in maxsulotlar.items():
    print(f"{maxsulot.capitalize()}ning narhi {narh}")

        
    
