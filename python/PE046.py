#!/usr/bin/env python
import math

def isPrime(n):
    if n < 2:
        return False
    m = int(math.sqrt(n))
    i = 2
    while i <= m:
        if n%i == 0:
            return False
        i += 1
    return True

def isCon(i):
    j = 1
    while 2*j*j < i:
        if isPrime(i-2*j*j):
            return True
        j += 1
    return False

def main():
    i = 35
    while True:
        if not isPrime(i) and not isCon(i):
            break
        i += 2
    print i

if __name__ == '__main__':
    main()
