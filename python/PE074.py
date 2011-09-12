#!/usr/bin/env python
L = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def factorialSum(n):
    global L
    res = 0
    while n != 0:
        res += L[n%10]
        n /= 10
    return res

D = {}
def length(n):
    global D
    t = [n]
    s = factorialSum(n)
    while s not in t:
        t.append(s)
        s = factorialSum(s)
        if s in D:
            D[n] = len(t) + D[s]
            break
    else:
        D[n] = len(t)
    return D[n]

def main():
    print sum(1 for i in range(1000000) if length(i) == 60)

if __name__ == '__main__':
    main()
