from math import factorial as fact
from keypad import *

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
        result = ''
        for value in sorted(romans.keys(), reverse=True):
            while n >= value:
                result += romans[value]
                n -= value
        return result 
    except:
        return 'Error!'   


def romanToDec(numStr):
    try:
        Dsum = 0
        for e in romVal:
            if numStr.find(e)==0:
                Dsum = Dsum + romVal[e]
                if len(e)==2:
                    numStr=numStr[2:]
                else:
                    numStr=numStr[1:]   
        return Dsum
    except:
        return 'Error!'
