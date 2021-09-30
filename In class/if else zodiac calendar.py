# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:02:25 2021

@author: larsm
"""

year = int(input("Enter a year: "))

if year < 0:
    print("print year is invalid")
else:
    if year % 12 == 8:
        animal = "Dragon"
    
    elif year % 12 == 9:
        animal = "Snake"
        
    elif year % 12 == 10:
        animal = "Horse"

    elif year % 12 == 11:
        animal = "Sheep"
        
    elif year % 12 == 0:
        animal = "Monkey"

    elif year % 12 == 1:
        animal = "Rooster"
        
    elif year % 12 == 2:
        animal = "Dog"
        
    elif year % 12 == 3:
        animal = "Pig"
        
    elif year % 12 == 4:
        animal = "Rat"
        
    elif year % 12 == 5:
        animal = "ox"
        
    elif year % 12 == 6:
        animal = "Tiger"
    else:
        animal = "Hare"
        
        
    if year == 2021:
        is_was = "is"
    elif year > 2021:
        is_was = "is gong to be"
    else:
        is_was = "was"
        
        
    print(f"{year} {is_was} the year of the {animal}")