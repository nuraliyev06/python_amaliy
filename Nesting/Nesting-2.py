# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 16:16:39 2025

@author: nuraliyev
"""
#1-topshiriqdagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
#For sikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

shaxs_1 = {'ismi' : 'albert einsteyn',
           'kasbi' : 'fizik',
           't_yil' : 1879,
           'vatani' : 'germaniya',
           'asarlari' : ['relativity theory', 'on the electrodynamics of moving bodies']}

shaxs_2 = {'ismi' : 'Usmon ibn Affon',
           'kasbi' : 'xalifa',
           't_yil' : 576,
           'vatani' : 'makka',
           'asarlari' : []}

shaxs_3 = {'ismi' : 'elon musk',
           'kasbi' : 'tadbirkor',
           't_yil' : 1971,
           'vatani' : 'jar',
           'asarlari' : []}

shaxs_4 = {'ismi' : 'abdulla qodiriy',
           'kasbi' : 'yozuvchi',
           't_yil' : 1894,
           'vatani' : "o'zbekiston",
           'asarlari' : ["o'tkan kunlar", 'mehrobdan chayon', 'juvonboz']}

mashxurlar = [shaxs_1, shaxs_2, shaxs_3, shaxs_4]

for shaxs in mashxurlar:
    ism = shaxs['ismi']
    if ism != 'Usmon ibn Affon' and len(shaxs['asarlari']) != 0:
        print(f"\n{ism.title()}ning mashxur asarlari:")
        for asar in shaxs['asarlari']:
            print(asar.title())
            
    elif ism == 'Usmon ibn Affon':
        print(f"\n{ism} birorta ham asar yozmagan.")
        
    else:
        print(f"\n{ism.title()} birorta ham asar yozmagan.")
        
        
        


