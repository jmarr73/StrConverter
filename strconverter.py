#!/usr/bin/env python3

# JMM (aka Hot Sauce)
# This script will take a line of characters and turn it into a list.
# From this point it is parse the data and return the Decimal and Hexadecimal values
# in a string seperated by commas.

# Text color changers
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prBrCyan(skk): print("\033[34m {}\033[00m" .format(skk))

# Add each character, and it's ordinal, of user's text input, to three lists
print("\r")
s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x
l1 = [] 
l2 = []
l3 = []
for c in s:   # in Python, a string is just a sequence, so we can iterate over it!
    l1.append(c) 
    l2.append(ord(c))
    l3.append(hex(ord(c)))
print("\r")
# print(l1)
# print(l2)
# print(l3)
pOrig = "Input to List: " + ','.join(map(str, l1))
print(pOrig)
#print("Dec Value(s): " + ','.join(map(str, l2)))
pDec = "Dec Value(s): " + ','.join(map(str, l2))
prBrCyan(pDec)
#print("Hex Value(s): " + ','.join(map(str, l3)))
pHex = "Hex Value(s): " + ','.join(map(str, l3))
prRed(pHex)
print("\r")