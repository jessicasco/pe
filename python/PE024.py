#!/usr/bin/python

def next(L):
    n = len(L)
    i = n - 1
    while L[i] <= L[i-1]:
        i -= 1
    j = n-1
    while L[j] < L[i-1]: 
        j -= 1
    t = L[j]
    L[j] = L[i-1]
    L[i-1] = t
    M = L[i:]
    M.sort()
    L = L[0:i] + M 
    return L

def main():
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1000000-1):
        L = next(L)
    print "".join([str(i) for i in L])

if __name__ == '__main__':
    main()
