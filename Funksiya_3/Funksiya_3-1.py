# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 11:18:30 2025

@author: nuraliyev
"""

def bosh_harf(royxat):
    bosh_harf = [ ]
    for ism in royxat:
        ism = ism.capitalize()
        bosh_harf.append(ism)
    return bosh_harf
        
ismlar = ['ali', 'vali', 'hasan', 'husan']

katta_harf = bosh_harf(ismlar)
print(katta_harf)
print(ismlar)