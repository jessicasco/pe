#!/usr/bin/env python
from PE007 import isPrime
def isTruncatable(n):
    m = str(n)
    while m != "":
        if not isPrime(int(m)):
            return False
        m = m[1:]
    m = str(n)
    while m != "":
        if not isPrime(int(m)):
            return False
        m = m[:-1]
    return True

def main():
    count = 0
    s = 0
    i = 11
    while count < 11:
        if isTruncatable(i):
            count += 1
            s += i
        i += 2
    print s

if __name__ == '__main__':
    main()
