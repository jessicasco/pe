#!/usr/bin/env python
from fractions import gcd
def main():
    n = 2
    d = 5
    for i in range(2,1000001):
        j = int(3.0/7.0*i)
        k = int(i*n*1.0/d)
        while j > k:
            if gcd(i,j) != 1:
                j -= 1
            else:
                if j*1.0/i > n*1.0/d and j*1.0/i < 3.0/7.0:
                    n = j
                    d = i
                break
    print n

if __name__ == '__main__':
    main()
