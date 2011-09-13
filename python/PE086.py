#!/usr/bin/env python
import math
def shortestDistance(ab, c):
    p = ab * ab + c * c
    d = int(math.sqrt(p))
    if d*d == p:
        return True
    return False
    
def main():
    M = 2
    count = 0
    while count <= 1000000:
        M += 1
        for i in range(3, 2*M+1):
            if shortestDistance(i, M):
                count += min(M, i-1) - int((i+1)/2) + 1
    print M

if __name__ == '__main__':
    main()
