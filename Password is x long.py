# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:43:39 2021

@author: larsm
"""

u = input("Enter username: ")
p = input("Enter password: ","\n")

print("Hello",u+". Your password ["+len(p)*"*"+"] is", len(p),"characters long.")