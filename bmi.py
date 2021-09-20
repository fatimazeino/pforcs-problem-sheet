# bmi.py
# This calculates somebody's Body Mass Index (BMI)
# Author: Fatima Zeino

height = float(input("Enter yor height in centimaters "))
height_maters = height/100
height_squared = height_maters*height_maters
weight = float(input("Enter your weight in kilograms "))
bmi = float(weight / height_squared)
txt = "your Body Mass Index is "
bmi_formatted = "{:.2f}".format(bmi)
print(txt + bmi_formatted)