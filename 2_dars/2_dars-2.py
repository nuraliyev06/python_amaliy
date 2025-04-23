# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 07:24:42 2025

@author: nuraliyev
"""
#5 ning 4-darajasini topuvchi kod

print(5**4)

#22ni 4 ga bo'lganda qancha qoldiq qolishini chiqaruvchi kod

print(22%4)

#tomonlari 125 ga teng bo'lgan kvadratning yuzi va perimetrini topuvchi kod

a=125
kvadratning_yuzi = 125**2
kvadratning_perimetri = 125*4

print(f"Tomonlari 125 ga teng bo'lgan kvadratning yuzi {kvadratning_yuzi} ga, "
    f"perimetri esa {kvadratning_perimetri} ga teng")

#diametri 12 bo'lgan doiraning yuzini toish uchun kod

diametr = 12
radius = diametr/2
pi = 3.14
doira_yuzi = pi*radius**2

print(f"Diametri {diametr} ga teng bo'lgan doiraning yuzi {doira_yuzi} ga teng")

#katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini topish uchun kod

a = 6 #uchburchakning birinchi kateti
b = 7 #uchburchakning ikkinchi kateti
c = (a**2 + b**2)**(1/2) #uchburchakning gipotenuzasi

print(f"Katetlari {a} va {b} bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi "
      f"{c} ga teng")
