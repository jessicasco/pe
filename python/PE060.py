#!/usr/bin/env python
from PE007 import isPrime
from PE010 import getPrimeList
def isConcatenatePrime(a, b):
    if isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a))):
        return True
    return False

def find(n, minimal, index):
    p = getPrimeList(n)
    length = len(p)
    for a in range(index, length):
        if minimal and p[a] > minimal/5:
            return True, minimal, a
        for b in range(a+1, length):
            if not isConcatenatePrime(p[a], p[b]):
                continue
            for c in range(b+1, length):
                if (not isConcatenatePrime(p[a], p[c]) 
                        or not isConcatenatePrime(p[b], p[c])):
                    continue
                for d in range(c+1, length):
                    if (not isConcatenatePrime(p[a], p[d])
                            or not isConcatenatePrime(p[b], p[d])
                            or not isConcatenatePrime(p[c], p[d])):
                        continue
                    for e in range(d+1, length):
                        if (not isConcatenatePrime(p[a], p[e])
                                or not isConcatenatePrime(p[b], p[e])
                                or not isConcatenatePrime(p[c], p[e])
                                or not isConcatenatePrime(p[d], p[e])):
                            continue
                        minimal = p[a] + p[b] + p[c] + p[d] + p[e]
                        break
    return False, minimal, length

def main():
    minimal = None
    index = 1
    n = 10000
    while True:
        flag, minimal, index = find(n, minimal, index)
        if flag:
            print minimal
            break
        n *= 10
        
if __name__ == '__main__':
    main()
