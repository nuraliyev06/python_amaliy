# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:33:30 2025

@author: nuraliyev
"""

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if str(qiymat).lower()=='exit':
        break
    
    elif int(qiymat)<0:
        continue
    
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
    
    