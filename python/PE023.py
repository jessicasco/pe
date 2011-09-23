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
    abundants = [i for i in range(1, 28123+1) if i < getSumOfProperDivisors(i)]
    abundantssum = set()
    for i in range(len(abundants)):
        a = abundants[i]
        if 2 * a > 28123:
            abundantssum.union(set(abundants[i:]))
            break
        for j in range(i, len(abundants)):
            a = abundants[i]
            b = abundants[j]
            if a+b > 28123:
                break
            abundantssum.add(a+b)
    print (1+28123)*28123/2 - sum(abundantssum)

if __name__ == '__main__':
    main()
