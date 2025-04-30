# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:41:04 2025

@author: nuraliyev
"""

#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
#harfini katta harfga o'zgatiruvchi funksiya yozing. 


def malumotlar(ism, familiya, t_yil, t_joy, e_mail = None, t_raqam = None):
    shaxs = {'ismi' : ism.capitalize(),
             'familiyasi' : familiya.capitalize(),
             't_yili' : t_yil,
             't_joyi' : t_joy.capitalize(),
             'e_maili' : e_mail,
             't_raqami' : t_raqam,
             'yoshi' : 2025 - t_yil}
    return shaxs

mijozlar = []

while True:
    
    ism = input('Ismingiz nima: ')
    familiya = input('Familiyangiz nima: ')
    t_yil = input('Nechanchi yilda tug\'ilgansiz: ')
    t_yil = int(t_yil)
    t_joy = input('Qayerda tug\'ilgansiz: ')
    savol = input("E-mailingizni kiritishni xohlaysizmi (xa/yo'q): ")
    if savol.lower() == 'xa':
        e_mail = input('Juda soz! E-mailingizni kiriting: ')
    elif savol.lower() == "yo'q":
        e_mail = None
    savol = input("Telefon raqamingizni kiritishni xohlaysizmi (xa/yo'q): ")
    if savol.lower() == 'xa':
        t_raqam = input('Juda soz! Telefon raqamingizni kiriting: ')
    elif savol.lower() == "yo'q":
        t_raqam = None
 
        

    
    mijozlar.append(malumotlar(ism, familiya, t_yil, t_joy, e_mail, t_raqam))
    
    savol = input("Yana ma'lumot qo'shamizmi (xa/yo'q): ")
    
    if savol.lower() == "yo'q":
        break
    
print("Bizning mijozlarimiz:")

for mijoz in mijozlar:
    if mijoz['e_maili'] == None:
        mijoz["e_maili"] = 'Kiritilmagan'
    
    if mijoz['t_raqami'] == None:
        mijoz['t_raqami'] = 'Kiritilmagan'
    
    
    print(f"{mijoz['ismi']} {mijoz['familiyasi']} {mijoz['t_joyi']}da tug'ilgan. "
          f"Hozirda {mijoz['yoshi']} yoshda.\n"
          f"Mijozning e-mail manzili: {mijoz['e_maili']}\n"
          f"Mijozning telefon raqami: {mijoz['t_raqami']}\n")
    
    



    

