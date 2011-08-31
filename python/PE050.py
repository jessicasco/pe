#!/usr/bin/env python
from PE007 import isPrime
from PE010 import getPrimeList

def main():
    t = getPrimeList(1000000)
    totallen = len(t)
    length = 0
    for i in range(totallen):
        if i+length >= totallen:
            break
        Sum = sum(t[i:i+length])
        for j in range(i+length, totallen):
            Sum += t[j]
            if Sum > 1000000:
                break
            if j-i+1 > length and isPrime(Sum):
                length = j-i+1
                Max = Sum
    print Max

if __name__ == '__main__':
    main()
