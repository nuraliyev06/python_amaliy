# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:53:42 2025

@author: nuraliyev
"""
friends = []

friends.append("Abdulhamid")
friends.append("Asilbek")
friends.append("Yaxyoxon")
friends.append("Azimjon")
friends.append("Jo'rabek")

#print(friends)

friends.remove("Azimjon")
friends.remove("Jo'rabek")

#print(friends)

friends.insert(0, "Samariddin")
friends.append("Shohruhmirzo")
friends.insert(2, "Boburmirzo")

#print(friends)

mehmonlar = []

mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(1))

print(mehmonlar)

