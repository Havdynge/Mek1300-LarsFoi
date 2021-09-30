# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:49:31 2021

@author: larsm
"""
print("Enter the appropriate for your car","\n")
gal = float(input("Number of gallons in the tank: ")) #20gal = 80liter
effi = float(input("The fuel efficiency in miles per gallon: ")) #20
price = float(input("The price of gas per gallon: ",)) #6$
print("")

print("The cost per 100 miles is:", "{:.2f}".format(price*(100/effi)))
print("The fuel range is: ", "{:.2f}".format(effi*gal))

