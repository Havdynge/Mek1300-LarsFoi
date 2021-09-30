# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:34:09 2021

@author: larsm
"""
RAISE_FACTOR = 2400
UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

rating = float(input("Enter your epmployee rating: "))

if rating == UNACCEPTABLE:
    performance = "Unacceptable"

elif rating == ACCEPTABLE:
    performance = "Accepteble"
    
elif rating >= MERITORIOUS:
    performance = "Meritorious"
else:
    performance = ""
    
if performance == "":
    print("That was not a valid rating!")
else:
    print("Based on you rating, your performance was", performance)
    print("You will recive a raise of $%0.2f" % (RAISE_FACTOR * rating))
