# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:13:18 2025

@author: nuraliyev
"""

def kattasini_chiqar(son1, son2, son3):
    
    if son1 > son2 and son1 > son3:
        print(son1)
    elif son2 > son1 and son2 > son3:
        print(son2)
    else:
        print(son3)

kattasini_chiqar(8902, -190, 2348)
    