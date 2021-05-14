# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Fatima Zeino

import math

def sqrt(num):
 tolerance = 0.000001
 x = 1.0
 while True:
  x = (x + num / x) / 2
  difference = abs(num - x ** 2)
  if difference <= tolerance:
       break
 return x
    
def main():
   while True:
       num = input("Enter a positive number or enter/return to quit: ")
       if not num:
         break
       num = float(num)
       print("The program's estimate is", sqrt(num))
       # print("Python's estimate is     ", math.sqrt(num))
main()


