#!/usr/bin/env python
from copy import deepcopy
from math import sqrt
def isT(t):
    n = int((-1 + sqrt(1 + 8*t))/2)
    if (n*(n+1))/2 == t:
        return True
    return False

def isS(t):
    n = int(sqrt(t))
    if n*n == t:
        return True
    return False

def isP(t):
    n = int((1+sqrt(1+24*t))/6)
    if (n*(3*n-1))/2 == t:
        return True
    return False

def isHex(t):
    n = int((1+sqrt(1+8*t))/4)
    if n*(2*n-1) == t:
        return True
    return False

def isHep(t):
    n = int((3+sqrt(9+40*t))/10)
    if (n*(5*n-3))/2 == t:
        return True
    return False

def isO(t):
    n = int((2+sqrt(4+12*t))/6)
    if n*(3*n-2) == t:
        return True
    return False

def ff(t, m):
    flag = False
    if isT(t):
        m[0].append(t)
        flag = True
    if isS(t):
        m[1].append(t)
        flag = True
    if isP(t):
        m[2].append(t)
        flag = True
    if isHex(t):
        m[3].append(t)
        flag = True
    if isHep(t):
        m[4].append(t)
        flag = True
    if isO(t):
        m[5].append(t)
        flag = True
    return flag

def main():
    for a in range(10,100):
        for b in range(10,100):
            m1 = [[], [], [], [], [], []]
            t = a * 100 + b
            if not ff(t, m1):
                continue
            for c in range(10,100):
                m2 = deepcopy(m1)
                t = b * 100 + c
                if not ff(t, m2):
                    continue
                for d in range(10,100):
                    m3 = deepcopy(m2)
                    t = c * 100 + d
                    if not ff(t, m3):
                        continue
                    for e in range(10,100):
                        m4 = deepcopy(m3)
                        t = d * 100 + e
                        if not ff(t, m4):
                            continue
                        for f in range(10,100):
                            m5 = deepcopy(m4)
                            t = e * 100 + f
                            if not ff(t, m5):
                                continue
                            t = f * 100 + a
                            if not ff(t, m5):
                                continue
                            for a1 in m5[0]:
                                for b1 in m5[1]:
                                    for c1 in m5[2]:
                                        for d1 in m5[3]:
                                            for e1 in m5[4]:
                                                for f1 in m5[5]:
                                                    x = {a1, b1, c1, d1, e1, f1}
                                                    if len(x) == 6:
                                                        print sum(x)
                                                        return
if __name__ == '__main__':
    main()
