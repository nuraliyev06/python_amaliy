# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:29:02 2025

@author: nuraliyev
"""

taomlar = ["palov", "shashlik", "manti", "lag'mon", "somsa"]
nonushta = taomlar[0:]
nonushta.remove('shashlik')
nonushta.remove('lag\'mon')
nonushta.remove('palov')

nonushta.append("qaymoqli non")
nonushta.append('omlet')

print(taomlar)


nonushta = tuple(nonushta)
print(nonushta)