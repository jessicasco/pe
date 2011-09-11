#!/usr/bin/env python
from PE007 import isPrime
from PE010 import getPrimeList

def isConcatenatePrime(a, b):
    if isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a))):
        return True
    return False

def f(n):
    p = getPrimeList(n)
    l = len(p)
    for n0 in range(l):
        for n1 in range(n0+1, l):
            if not isConcatenatePrime(p[n0], p[n1]):
                continue
            for n2 in range(n1+1, l):
                if (not isConcatenatePrime(p[n0], p[n2]) 
                        or not isConcatenatePrime(p[n1], p[n2])):
                    continue
                for n3 in range(n2+1, l):
                    if (not isConcatenatePrime(p[n0], p[n3])
                            or not isConcatenatePrime(p[n1], p[n3])
                            or not isConcatenatePrime(p[n2], p[n3])):
                        continue
                    for n4 in range(n3+1, l):
                        if (not isConcatenatePrime(p[n0], p[n4])
                                or not isConcatenatePrime(p[n1], p[n4])
                                or not isConcatenatePrime(p[n2], p[n4])
                                or not isConcatenatePrime(p[n3], p[n4])):
                            continue
                        print p[n0] + p[n1] + p[n2] + p[n3] + p[n4]
                        return True
    return False

def main():
    n = 10000
    while True:
        res = f(n)
        if res:
            break
        n *= 10
        
if __name__ == '__main__':
    main()
