#!/usr/bin/env python
import math

def isPentagonal(n):
    t = (1 + int(math.sqrt(1+24*n)))/6;
    if t*(3*t-1)/2 == n:
        return True
    return False

def main():
    pentagonal = [0]
    i = 1
    Min = None
    while True:
        pentagonal.append(i*(3*i-1)/2)
        m = pentagonal[-1] - pentagonal[-2]
        if Min and m >= Min:
            break
        j = i - 1
        while j > 0:
            m = pentagonal[i] - pentagonal[j]
            if Min and m >= Min:
                break
            n = pentagonal[i] + pentagonal[j]
            if isPentagonal(m) and isPentagonal(n):
                Min = m
            j -= 1
        i += 1
    print Min

if __name__ == '__main__':
    main()
