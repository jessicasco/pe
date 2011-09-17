#!/usr/bin/env python
import math
 
def main():
    n = 35 + 85
    sqrt2 = 1.0 / math.sqrt(2)
    while True:
        x = int(sqrt2 * n) + 1
        if 2*x*(x-1) == n*(n-1):
            result = x
            if n > 10**12: 
                break
            n = int(5.8284 * n)
        n += 1
    print result

if __name__ == '__main__':
    main()
