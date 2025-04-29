# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 12:05:57 2025

@author: nuraliyev
"""

def bolinishni_tekshirish(son):
    
    """Sonning 2 dan 10 gacha bo'lgan sonlardan qaysi biriga qoldiqsiz
    bo'linishini hisoblaydian funksiya"""
    
    for n in range(2, 11):
        if son % n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi.")
            
bolinishni_tekshirish(15)
