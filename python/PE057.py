#!/usr/bin/env python
from fractions import gcd
def main():
    num = 1
    den = 2
    count = 0
    for i in range(1000):
        if len(str(num + den)) > len(str(den)):
            count += 1
        tmp = den
        den = 2 * den + num
        num = tmp
        tmp = gcd(num, den)
        den /= tmp
        num /= tmp 
    print count

if __name__ == '__main__':
    main()
