#!/usr/bin/env python
from PE009 import getPythagoreanTriplet
def isTrue(s):
    return sum(1 for i in getPythagoreanTriplet(s)) == 1

def main():
    print sum(1 for i in range(12, 1500001, 2) if isTrue(i))

if __name__ == '__main__':
    main()
