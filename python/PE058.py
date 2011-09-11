#!/usr/bin/env python
from PE007 import isPrime

def main():
    step = 2
    n = 1
    count = 0
    while True:
        for i in range(4):
            if isPrime(n + i * step + step):
                count += 1
        ratio = count*1.0/(step/2*4+1) 
        if ratio < 0.1:
            print step + 1
            return
        n += 4 * step
        step += 2

if __name__ == '__main__':
    main()
