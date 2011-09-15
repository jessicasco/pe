#!/usr/bin/env python
import math
def main():
    smax = int(math.sqrt(166666666))+1
    p = 0
    for s in xrange(1,smax):
        s2 = s**2
        r1 = math.sqrt(3*s2+1)
        r_1 = math.sqrt(3*s2-1)
        for x in [int(y) for y in [r1,r_1] if int(y) == y]:
            for r in [2*s+x,2*s-x,x]:
                r2 = r**2
                if r>s and 3*(s2 + r2)<1e9:
                    p += 2*(s2 + r2) + 2*min(r2-s2,2*r*s)
    print p

if __name__ == '__main__':
     main()
