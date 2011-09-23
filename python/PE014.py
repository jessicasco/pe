#!/usr/bin/env python
def main():
    data = {}
    maxlen = 0
    for i in range(1, 1000000):
        length = 1
        n = i
        while n != 1:
            if n in data:
                length =  length + data[n]
                break
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            length += 1
        data[i] = length
        if length > maxlen:
            maxlen = length
            maxnum = i
    print maxnum

if __name__ == '__main__':
    main()
