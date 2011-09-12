#!/usr/bin/env python
from PE010 import getPrimeList

primeList = None
D = {}

def f(i,m):
    global primeList, D
    if (i, m) in D:
        return D[(i,m)]
    count = 0
    for j in primeList:
        if j > i or j > m:
            break
        elif j == i:
            count += 1
        else:
            count += f(i-j, j)
    D[(i, m)] = count
    return count

def main():
    global primeList
    n = 10000
    primeList = getPrimeList(n)
    i = 2
    while f(i, i-1) <= 5000:
        i += 1
        if i > primeList[-1]:
            n *= 10
            primeList = getPrimeList(n)
    print i

if __name__ == '__main__':
    main()
