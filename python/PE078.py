#!/usr/bin/env python
"""
use the function form PE076 doesn't make sense, that takes too long.
"""
"""
p(0) = 1; p(k) = 0, (k<=0)
p(n) = p(n-1) + p(n-2) -p(n-5) -p(n-7) + ... +
p(n) = (-1)^(k-1)*p(n-(3*k*k-k)/2) + (-1)^(k-1)*p(n-(3*k*k+k)/2)+...(n>=1)
"""
L = {}
L[0] = 1
def p(n):
    global L
    if n < 0:
        return 0
    if n in L:
        return L[n]
    k = 1
    count = 0
    flag = 1
    while True:
        n1 = (3*k*k-k)/2
        n2 = (3*k*k+k)/2
        count += flag*(p(n-n1)+p(n-n2))
        flag *= -1
        if n2 >= n:
            break
        k += 1
    L[n] = count
    return count

def main():
    i = 2
    while p(i)%1000000:
        i += 1
    print i

if __name__ == '__main__':
    main()
