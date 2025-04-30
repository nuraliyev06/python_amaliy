# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:13:28 2025

@author: nuraliyev
"""

def talaba(ism, familiya, **qoshimcha):
    qoshimcha["ismi"] = ism
    qoshimcha['familiyasi'] = familiya
    return qoshimcha

talaba = talaba('Abdulhamid', 'Adhamov', t_yil = 2005)
print(talaba)
    
    
