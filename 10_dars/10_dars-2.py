# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 18:19:23 2025

@author: nuraliyev
"""
#Foydalanuvchidan yoshini so'rang, va muzeyga kirish uchun chipta narxini
#quyidagicha chiqaring:
    #Agar foydalanuvchi 4 yoshdan kichkina yoki 60 yoshdan katta bo'lsa bepul
    #Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    #Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingizni kiriting: "))


if yosh < 4 or yosh > 60:
    print("Sizga kirish bepul")
elif yosh < 18:
    narh = 10000
    print(f"Sizga kirish {narh} so'm")
else:
    narh = 20000
    print(f"Sizga kirish {narh} so'm")
