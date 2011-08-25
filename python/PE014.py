#!/usr/bin/env python

data = {}
def getLength(n):
    length = 1
    while n != 1:
        if n in data:
            return length + data[n]
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        length += 1
    return length

def main():
    maxlen = 0
    for i in range(1, 1000000):
        length = getLength(i)
        data[i] = length
        if length > maxlen:
            maxlen = length
            maxnum = i
    print maxnum

if __name__ == '__main__':
    main()
