#!/usr/bin/env python

"""
references:
    http://mathworld.wolfram.com/FactorialSums.html
    http://mathworld.wolfram.com/Factorion.html
"""

def main():
    f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s = 0
    for a in range(3, f[-1]*7):
        if a == sum(f[int(i)] for i in str(a)):
            s += a
    print s

if __name__ == '__main__':
    main()
