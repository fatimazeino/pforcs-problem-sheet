# es.py
# This program reads in a text file and outputs the number of e's it contains
# Author: Fatima Zeino

import sys
import os.path

# This will get the last argument on the command line. If no arguments are passed,
# it will be the script name itself, as sys.argv[0] is the name of the running program
filename = sys.argv[-1]
#print(filename)

def readNumber():
    try:
        with open(filename) as f:
            data = f.read().count('e\'s')
            return data
    except IOError:
        return 0

if not os.path.isfile(filename):
 print("File does not exist")
else :
 print("the number of e\'s in the text file are ", readNumber())