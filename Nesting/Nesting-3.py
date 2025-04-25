# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:45:07 2025

@author: nuraliyev
"""
#Do'stlaringizdan 3 ta sevimli filmlarini so'rang. Do'stingiz ismi kalit, uning
#seviml kinolarini esa ro'yxat ko'rinishida lug'atga saqlang. Natijani konsolga chiqaring.

sevimli_kinolar = {
    'abdulhamid' : ['arcane', 'naruto', 'jinoyat va jazo'],
    'rustamjon' : ['t-34', 'ellona xolms', 'tubanlik'],
    'muhammadyusuf' : ['matritsa', 'interstellar', 'substansiya'],
    'shohjahon' : ['mening dadam bo\'ydoq', 'boyvachcha kuyov', 'katta hovli']}

for ism, kinolar in sevimli_kinolar.items():
    print(f"\n{ism.capitalize()}ning yoqtirgan filmlari:")
    for kino in kinolar:
        print(kino.capitalize())
