# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 18:39:28 2025

@author: nuraliyev
"""
#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi 
#stop so'zini yozishi bilan dasturni to'xtating.
print('Yoqtirgan kitoblaringiz ro\'yxatini tuzamiz')

kitoblar=[]

son = 1


while True:
    savol = f"{son}-kitob nomini kiriting(dasturni tugatish uchun 'stop' "
    savol += "deb yozing): "
    son += 1
  
    kitob = input(savol)
    if kitob.lower() == 'stop':
        break
    
    else:
        kitoblar.append(kitob)

tugadi = 'Dastur tugadi!'
print(tugadi)
    
    
        