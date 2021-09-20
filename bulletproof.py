# bulletproof.py
# This program 
# Author: Fatima Zeino

import logging


def listEnter():
    theList = []
    listLen = int(input("Enter list's length : "))
    for i in range(0,listLen):
      element = float(input("Enter item : "))
      theList.append(element)
    #print(aList)
    return theList

def IndexEnter():
    toIndex = input('Enter a Index : ')
    return toIndex


def averageTo(aList, toIndex):
    result = 0
    aList.append(toIndex)
    for item in aList:
        result += float(item)
        averageNum = result / len(aList)
    logging.debug("%d: %s",aList , toIndex)
    return int(averageNum)