# testbulletproof.py
# This program test bulleproof class and response to some invalid input entered
# Author: Fatima Zeino

import bulletproof as bp

def toDo():
  aList = bp.listEnter()
  toIndex = bp.IndexEnter()
  avergeList = bp.averageTo(aList, toIndex)

  print ('the averge of {} incluing {} is {}'.format(aList, toIndex, avergeList))

try:
  toDo()
except ValueError:
 print('Invalid value intered')
 #print('Please be careful and enter the values agian :) ')
 #toDo()
 pass
#else:

 #assert False, 'Hi'