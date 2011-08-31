#!/usr/bin/env python
from PE007 import isPrime

def nextCircular(n):
    s = str(n)
    s = s[-1] + s[0:-1]
    return int(s)

def isCircularPrime(n):
    m = n
    while isPrime(m):
        m = nextCircular(m)
        if n == m:
            return True
    return False

def main():
    count = 0
    for i in range(2, 1000000):
        if isCircularPrime(i):
            count += 1
    print count

if __name__ == '__main__':
    main()
