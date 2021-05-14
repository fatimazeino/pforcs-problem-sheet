# bmi.py
# This program takes height in cm 
# convert height to m
# squraed height 
# take weight
# weight divided by  height in squared.
# take two numbers after decimal point
# Author: Fatima Zeino

height = float(input("Enter yor height in centimaters "))
height_maters = height/100
height_squared = height_maters*height_maters
weight = float(input("Enter your weight in kilograms "))
bmi = float(weight / height_squared)
txt = "your Body Mass Index is "
bmi_formatted = "{:.2f}".format(bmi)
print(txt + bmi_formatted)