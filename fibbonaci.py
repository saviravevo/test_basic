# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:38:20 2018

@author: Savira Hanandita
"""
def fib(n:'hingga nomor n')->int:
    l=[0,1]
    if n==0:
        return l[0]
    elif n==1:
        return l
    a=0
    b=1
    for i in range(0,n-1):
        b=a+b
        a=b-a
        l.append(b)
    return l