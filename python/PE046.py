#!/usr/bin/env python
from PE007 import isPrime

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
