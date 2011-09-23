#!/usr/bin/env python
import math
def isT(n):
    x = int((-1+math.sqrt(1+8*n))/2)
    if x*(x+1)/2 == n:
        return True
    return False

def isP(n):
    x = int((1+math.sqrt(1+24*n))/6)
    if x*(3*x-1)/2 == n:
        return True
    return False

def H(n):
    return n*(2*n-1)

def main():
    i = 144
    h = H(i)
    while not isT(h) or not isP(h):
        i += 1
        h = H(i)
    print h

if __name__ == '__main__':
    main()
