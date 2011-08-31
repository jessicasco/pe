#!/usr/bin/env python
from PE007 import isPrime

def main():
    t = []
    for i in range(2, 1000000):
        if isPrime(i):
            t.append(i)
    length = 0
    for i in range(len(t)):
        Sum = sum(t[i:i+length])
        for j in range(i+length, len(t)):
            Sum += t[j]
            if Sum > 1000000:
                break
            if isPrime(Sum) and j-i+1 > length:
                length = j-i+1
                Max = Sum
    print Max

if __name__ == '__main__':
    main()
