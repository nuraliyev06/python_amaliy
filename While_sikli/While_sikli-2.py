# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:18:18 2025

@author: nuraliyev
"""

#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
#7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday 
#while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini 
#chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin 
#(ikkita shartni ham tekshiring).

while True:
    savol = ('Yoshingizni kiriting (dasturni to\'xtatish uchun "exit" yoki "quit" deb yozing): ')
    yosh = input(savol)
    
    if yosh == 'exit' or yosh == 'quit':
        
        break
    
    else:
        
        yosh = int(yosh)
        
        if yosh < 7:
            narh = 2000
        
        elif yosh < 18:
            narh = 3000
            
        elif yosh < 65:
            narh = 10000
        
        else:
            narh = 0
        
        print(f"Sizga kirish narxi {narh} so'm!")
    
