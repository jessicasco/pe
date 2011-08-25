#!/usr/bin/env python

"""
N = p1^a1 * p2^a2 * p3^a3 * ...
The number of divisor  D(N) = (a1 + 1) * (a2 + 1) * (a3 + 1) * ...
"""

def triangle(n):
    return (n * (n+1)) / 2

def numOfdivisors(n):
    res = 1
    c = 1
    while n % 2 == 0:
        n /= 2
        c += 1
    res *= c
    i = 3
    while i*i <= n and n > 1:
        c = 1
        while n % i == 0:
            n /= i
            c += 1
        res *= c
        i += 2
    if n > 1:
        res *= 2
    return res

def main():
    i = 1
    while numOfdivisors(triangle(i)) <= 500:
        i += 1
    print triangle(i)

if __name__ == '__main__':
    main()
