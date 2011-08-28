#!/usr/bin/env python
import math

def isTriangle(n):
    t = int((-1+math.sqrt(1+8*n))/2)
    if n == (t*(t+1))/2:
        return True
    return False

def main():
    s = open("PE042.txt").readline().split(",")
    count = 0
    for t in s:
        Sum = 0
        for c in t:
            if c >= 'A' and c <= 'Z':
                Sum += ord(c) - ord('A') + 1
        if isTriangle(Sum):
            count += 1
    print count

if __name__ == '__main__':
    main()
