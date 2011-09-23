#!/usr/bin/env python
from PE007 import isPrime
def g(a, b, n):
    return n*n + a*n + b

def f(a, b):
    n = 0
    while isPrime(g(a, b, n)):
        n += 1
    return n

def main():
    maxLen = 0
    for a in range(-999, 1000):
        for b in range(2, 1000):
            length = f(a, b)
            if length > maxLen:
                maxLen = length
                c, d = a, b
    print c * d
    
if __name__ == '__main__':
    main()
