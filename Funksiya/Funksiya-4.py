# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:44:56 2025

@author: nuraliyev
"""
#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
#funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.



def taqqoslash(son1, son2):
    if son1 < son2:
        print(f"{son1} < {son2}")
    
    elif son1 > son2:
        print(f"{son1} > {son2}")
        
    else:
        print('Sonlar teng.')
        
taqqoslash(2, 2)
    
    