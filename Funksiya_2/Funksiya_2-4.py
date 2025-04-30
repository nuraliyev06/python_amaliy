# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:27:33 2025

@author: nuraliyev
"""

def tub_son(son1, son2):
    tub_sonlar = []
    for n in range(son1, son2):
        if n>1:
            for boluvchi in range(2, n):
                if n % boluvchi ==0:
                    break
            else:
                tub_sonlar.append(n)
            
        
            
    return tub_sonlar


tub = tub_son(1,10)
print(tub)

        
        
