#!/usr/bin/env python
from fractions import gcd
def main():
    count = 0
    for d in range(2, 12001):
        up = d / 2 + 1
        down = d / 3 - 1
        while up >= down:
            if gcd(up, d) == 1 and up*1.0/d > 1.0/3 and up*1.0/d < 1.0/2:
                count += 1
            up -= 1
    print count

if __name__ == '__main__':
    main()
