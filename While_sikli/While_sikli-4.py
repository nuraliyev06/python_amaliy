# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:42:07 2025

@author: nuraliyev
"""
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini 
#birma-bir qabul qilib, yangi ro'yxatga joylang.

savol = "Buyurtma iqlmoqchi bo'lgan maxsulotingizning nomini kiriting\n"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

buyurtmalar = []

while True:
    
    
    buyurtma = input(savol)
    if buyurtma.lower() != 'exit':
        buyurtmalar.append(buyurtma)
    
    else:
        break
    
