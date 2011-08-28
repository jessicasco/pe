#!/usr/bin/env python

def main():
    s = ""
    i = 1
    while len(s) < 1000000:
        s += str(i)
        i += 1
    res = 1
    for i in range(7):
        res *= int(s[pow(10, i)-1])
    print res

if __name__ == '__main__':
    main()
