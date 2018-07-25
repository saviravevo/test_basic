# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:38:20 2018

@author: Savira Hanandita
"""
#input dari user
num = int(input("Masukkan angka: "))

# bilangan prima yang lebih dari 1
if num > 1:   
# mengecek faktor   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"bukan bilangan prima")
           print("karena", i,"dikali",num//i,"adalah",num)
           break
   else:
       print(num,"adalah bilangan prima")
# jika input number <=1 maka bukan bilangan prima
else:
   print(num,"bukan bilangan prima")