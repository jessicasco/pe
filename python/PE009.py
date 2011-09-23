#!/usr/bin/env python
"""
Pythagorean Triplet(a, b, c): a*a + b*b == c*c.

Primitive: a = m*m-n*n, b = 2*m*n, c = m*m+n*n, m > n > 0, 
    exactly one of m, n is even and gcd(m,n) = 1.

We define a function which yields pythagorean triplet(a,b,c) 
whose sum(a+b+c) is s, 
a = (m*m-n*n)*d, b = 2*m*n*d, c = (m*m+n*n)*d
So a+b+c=2*m*(m+n)*d
So to find a pythagorean triplet (a,b,c) with a+b+c=s, 
we have to find a divisor m(>1) of s/2 and an odd divisor k(=m+n) of s/(2*m) 
with m<k<2*m and gcd(m,k)=1. 
Then set n=k-m, d=s/(2*m*k) and plug these in the previous 
representation of (a,b,c)
"""
import math, fractions
def getPythagoreanTriplet(s):
    s2 = s / 2
    mlimit = int(math.ceil(math.sqrt(s2)))
    for m in range(2, mlimit):
        if s2 % m == 0:
            sm = s2 / m
            while sm % 2 == 0:
                sm /= 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2*m and k <= sm:
                if sm % k == 0 and fractions.gcd(k, m) == 1:
                    d = s2 / (k*m)
                    n = k - m
                    a = d * (m*m - n*n)
                    b = 2 * d * m * n
                    c = d * (m*m + n*n)
                    yield (a, b, c, )
                k += 2

def main():
    for a, b, c in getPythagoreanTriplet(1000):
        print a * b * c

if __name__ == '__main__':
    main()
