#!/usr/bin/env python
def main():
    n = map(int, ''.join(open("PE008.txt").read().splitlines()))
    l = len(n)
    maxProduct = 0
    i = 0
    while i <= l-5:
        current = n[i] * n[i+1] * n[i+2] * n[i+3] * n[i+4]
        if current > maxProduct:
            maxProduct = current
        i += 1
    print maxProduct

if __name__ == '__main__':
    main()
