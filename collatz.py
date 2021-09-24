# collatz.py
# This program outputs the successive values of the some calculation
# Author: Fatima Zeino

val = int(input("enter any positive integer "))

print (val)

while val != 1 :

    if val % 2 == 0 :
        val = int (val / 2)
        print (val)
    elif val % 2 != 0 :
        val = int (( val * 3 ) + 1)
        print (val)

print("The end")