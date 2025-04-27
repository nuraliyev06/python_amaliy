# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:58:02 2025

@author: nuraliyev
"""

maxsulotlar = {}

savol = "Maxsulotingizni kiriting"
savol += "(chiqish uchun 'exit' deb yozing): "

while True:
    maxsulot = input(savol)
    if maxsulot.lower() != 'exit':
        narh = input(f"{maxsulot.capitalize()}ning narhini kiriting: ")
        maxsulotlar[maxsulot] = int(narh)
    else:
        break

savol = "Buyurtma qilmoqchi bo'lgan maxsulotingizning nomini kiriting\n"
savol += "(narxlarni bilish uchun 'okey' deb yozing): "

buyurtmalar = []

while True:
    
    
    buyurtma = input(savol).lower()
    if buyurtma != 'okey':
        buyurtmalar.append(buyurtma)
    
    else:
        break
    
for buyurtma in buyurtmalar:
    if buyurtma in maxsulotlar:
        narh = maxsulotlar[buyurtma.lower()]
        print(f"{buyurtma.capitalize()}ning narxi {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q!")