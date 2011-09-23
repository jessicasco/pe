#!/usr/bin/env python
def lengthOfRecurringCycle(n):
    L = []
    s = 10
    while (s/n, s%n) not in L:
        L.append((s/n, s%n))
        s = s%n
        s *= 10
        if s == 0:
            return 0
    for i in range(len(L)):
        if L[i] == (s/n, s%n):
            return len(L)-i

def main():
    maxLen = 0
    for i in range(2, 1000):
        length = lengthOfRecurringCycle(i) 
        if length >= maxLen:
            maxLen = length
            maxNum = i
    print maxNum

if __name__ == '__main__':
    main()
