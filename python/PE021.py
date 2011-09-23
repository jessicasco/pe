#!/usr/bin/env python
"""
Let d(n) be the sum of divisors of n
1. For any prime, p: d(p) = p + 1
2. For any prime, p: d(p^a) = p + p^2 + p^3 + ... + p^a = (p^(a+1) - 1)/(p-1)
3. d(a*b*...) = d(a) * d(b) * ..., where a,b,..., are relatively prime.
"""

def getSumOfDivisors(n):
    s = 1
    p = 2
    while p*p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n /= p
            while n % p == 0:
                j *= p
                n /= p
            s *= j - 1
            s /= p - 1
        if p == 2:
            p = 3
        else: 
            p += 2
    if n > 1:
        s *= n + 1
    return s

def getSumOfProperDivisors(n):
    return getSumOfDivisors(n) - n

def main():
    s = 0
    for i in range(1, 10000):
        n = getSumOfProperDivisors(i)
        if n > i and i == getSumOfProperDivisors(n):
            s += i + n
    print s

if __name__ == '__main__':
    main()
