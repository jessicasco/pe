#!/usr/bin/env python
from fractions import gcd
def solve_pell():
    num = 1
    den = 2
    while True:
        if (num+den)*(num+den) - 2*den*den == 1:
            return num+den, den
        tmp = den
        den = 2 * den + num
        num = tmp
        tmp = gcd(num, den)
        den /= tmp
        num /= tmp 

def main():
    a, b = solve_pell()
    total = 120
    tt = 2*120-1
    blue = 85
    bb = 2*85-1
    while total <= 1000000000000:
        temp = a*tt + 2*b*bb
        bb = b*tt + a*bb
        tt = temp
        total = (tt+1)/2
        blue = (bb+1)/2
    print blue

if __name__ == '__main__':
    main()
