# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:39:36 2025

@author: nuraliyev
"""
#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
#funksiya yozing.



def toq_juft(son):
    son = int(son)
    
    if son % 2 == 0:
        print('Juft son')
    
    else:
        print('Toq son')

toq_juft(5)
