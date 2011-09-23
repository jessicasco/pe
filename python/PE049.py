#!/usr/bin/env python
from PE007 import isPrime
def isPerm(i, j):
    a = sorted(list(str(i)))
    b = sorted(list(str(j)))
    return a == b

def main():
    for i in range(1000, 10000):
        for j in range (1, (10000-i)/2):
            if isPrime(i) and isPrime(i+j) and isPrime(i+2*j):
                if isPerm(i, i+j) and isPerm(i, i+2*j) and not (i == 1487 and j == 3330):
                    print str(i)+str(i+j)+str(i+2*j)
                    return

if __name__ == '__main__':
    main()
