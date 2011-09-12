#!/usr/bin/env python
"""
Euler's totient function:
    http://en.wikipedia.org/wiki/Euler's_totient_function
"""
from PE010 import getPrimeList
def main():
    primelist = getPrimeList(1000000)
    res = [i for i in range(2,1000001)]
    for i in range(len(primelist)):
        l = primelist[i]
        m = l
        while l <= 1000000:
            res[l-2] *= (m-1)
            res[l-2] /= m
            l += m
    maximum = 0
    for i in range(len(res)):
        if (i+2)*1.0/res[i] > maximum:
            maximum = (i+2)*1.0/res[i]
            maxn = i+2
    print maxn

if __name__ == '__main__':
    main()
