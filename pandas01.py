# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:27:11 2024

@author: pjcp0
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

#print(df.describe())

age = [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
print(age)

print(age[0])
print(age[1])
print(age[10])

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

C2="M"
C3="M"
C4="F"
print(C2)
print(C3)
print(C4)

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

#Country list

country = ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique","Lesotho","Kenya", "Kenya", "Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])

