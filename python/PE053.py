#!/usr/bin/env python

def comb(n, r):
    res = 1.0
    for i in range(r):
        res *= (n-i)*1.0/(i+1)
    return int(res)

def main():
    count = 0
    for i in range(23, 101):
        j = i / 2
        while comb(i, j) >= 1000000:
            if 2*j != i:
                count += 1
            count += 1
            j -= 1
    print count

if __name__ == '__main__':
    main()
