#!/usr/bin/env python

def numOfSolution(n):
    count = 0
    for a in range(3, n/3):
        for b in range(a+1, (n-a+1)/2):
            c = n - a - b
            if a*a + b*b == c*c:
                count += 1
    return count

def main():
    Max = 0
    for i in range(12, 1001):
        if numOfSolution(i) > Max:
            Max = numOfSolution(i)
            MaxP = i
    print MaxP

if __name__ == '__main__':
    main()
