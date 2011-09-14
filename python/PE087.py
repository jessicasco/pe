#!/usr/bin/env python
from PE010 import getPrimeList
def main():
    N = 50000000
    primelist = getPrimeList(N ** 0.5)
    square = []
    cube = []
    fourthpower = []
    for p in primelist:
        a = p*p
        if a >= N:
            break
        square.append(a)
        if a*p <= N:
            cube.append(a*p)
            if a*p*p <= N:
                fourthpower.append(a*p*p)
    count = []
    for c in fourthpower:
        for b in cube:
            if c+b >= N:
                break
            for a in square:
                if c+b+a >= N:
                    break
                count.append(c+b+a)
    print len(set(count))


if __name__ == '__main__':
    main()
