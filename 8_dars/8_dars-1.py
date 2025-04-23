# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:53:10 2025

@author: nuraliyev
"""

#kamida 5 ta elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har
#bir ismga takrorlanuvchi xabar yozing.

ismlar = ["Muhammadyusf", "Abdulhamid", "Shohjahon", "Rustanjon", "Dilshodbek"]

for ism in ismlar:
    print(f"Salom, {ism}")

#Yuqoridagi sikl tugaganidan so'ng ekranga "Kod n marta takrorlandi" degan
#xabarni chiqaring. (n o'rnifa kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")
