#!/usr/bin/env python

def main():
    n = 600851475143
    m = 1
    i = 3
    while i*i <= n:
        while n % i == 0:
            n /= i
            m = i
        i += 2
    if n != 1:
        print n
    else:
        print m

if __name__ == '__main__':
    main()
