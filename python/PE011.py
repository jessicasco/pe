#!/usr/bin/env python
import os

def isValid(a, b):
    if a >= 0 and a <= 19 and b >= 0 and b <= 19:
        return True
    return False

def main():
    datafile = os.path.abspath(__file__)[:-2] + 'txt'
    data = [map(int, line[:-1].split()) for line in open(datafile)]
    maxProduct = 0
    for a in range(20):
        for b in range(20):
            if isValid(a-3, b+3):
                c = data[a][b]*data[a-1][b+1]*data[a-2][b+2]*data[a-3][b+3]
                if c > maxProduct:
                    maxProduct = c
            if isValid(a, b+3):
                c = data[a][b]*data[a][b+1]*data[a][b+2]*data[a][b+3]
                if c > maxProduct:
                    maxProduct = c
            if isValid(a+3, b+3):
                c = data[a][b]*data[a+1][b+1]*data[a+2][b+2]*data[a+3][b+3]
                if c > maxProduct:
                    maxProduct = c
            if isValid(a+3, b):
                c = data[a][b]*data[a+1][b]*data[a+2][b]*data[a+3][b]
                if c > maxProduct:
                    maxProduct = c

    print maxProduct

if __name__ == '__main__':
    main()
