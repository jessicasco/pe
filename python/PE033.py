#!/usr/bin/env python
from fractions import gcd
def main():
    n = 1
    d = 1
    for a in range(10, 100):
        for b in range(a+1, 100):
            if (b%10 != 0 and  a%10 == b/10 and  a*1.0/b == (a/10)*1.0/(b%10) 
                    and a*1.0/b != (a/10)*1.0/(b/10)):
                n *= a
                d *= b
    print d / gcd(d, n)

if __name__ == '__main__':
    main()
