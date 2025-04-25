# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 15:54:21 2025

@author: nuraliyev
"""
#Adabiyot(ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar haqidagi ma'lumotlarni
#lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang va har bir shaxs
#haqidagi ma'lumotlarni konsolga chiqaring.

shaxs_1 = {'ismi' : 'albert einsteyn',
           'kasbi' : 'fizik',
           't_yil' : 1879,
           'vatani' : 'germaniya'}

shaxs_2 = {'ismi' : 'Usmon ibn Affon',
           'kasbi' : 'xalifa',
           't_yil' : 576,
           'vatani' : 'makka'}

shaxs_3 = {'ismi' : 'elon musk',
           'kasbi' : 'tadbirkor',
           't_yil' : 1971,
           'vatani' : 'jar'}

shaxs_4 = {'ismi' : 'abdulla qodiriy',
           'kasbi' : 'yozuvchi',
           't_yil' : 1894,
           'vatani' : "o'zbekiston"}

mashxurlar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4]

for shaxs in mashxurlar:
    if shaxs['ismi'] != 'elon musk':
        
        if shaxs['ismi'] != 'Usmon ibn Affon':
            xabar = f"{shaxs['ismi'].title()} {shaxs['t_yil']}-yilda {shaxs['vatani']}da tug'ilgan, {shaxs['kasbi']} bo'lgan."
            print(xabar)
            
        else:
            xabar = f"{shaxs['ismi']} {shaxs['t_yil']}-yilda {shaxs['vatani']}da tug'ilgan, {shaxs['kasbi']} bo'lgan."
            print(xabar)
            
    else:
        shaxs['vatani'] = shaxs['vatani'].upper()
        xabar = f"{shaxs['ismi'].title()} {shaxs['t_yil']}-yilda {shaxs['vatani']}da tug'ilgan, hozirda {shaxs['kasbi']}."
        print(xabar)
        
            
            
            
            
            