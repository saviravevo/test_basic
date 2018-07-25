# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:38:20 2018

@author: Savira Hanandita
"""

angka = str(1345679)
x = (len(angka)-1)
while x > 0:
    for a in angka:
        print(a+('0' * x))
        x -= 1