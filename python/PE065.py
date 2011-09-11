#!/usr/bin/env python
from fractions import gcd

def main():
    d = 0
    n = 1
    for i in range(33):
        j = (33-i)*2
        tmp = n + j * (n + d)
        n = tmp + n + d
        d = tmp
        tmp = gcd(n, d)
        n /= tmp
        d /= tmp
    
    tmp = d + 2 * n
    d = n
    n = tmp
    tmp = gcd(d, n)
    n /= tmp
    d /= tmp
    print sum(int(i) for i in str(n))
    
if __name__ == '__main__':
    main()
