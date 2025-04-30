# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:04:32 2025

@author: nuraliyev
"""
def kopaytir(*sonlar):
    
    natija = 1
    for son in sonlar:
        natija = son*natija
    
    return natija
natija = kopaytir(2,3,5)
print(natija)
        
        
