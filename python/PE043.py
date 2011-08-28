#!/usr/bin/env python

def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i+1:]
            for p in perm(rest, n-1):
                yield v + p

def main():
    t = [2, 3, 5, 7, 11, 13, 17]
    Sum = 0
    a = perm("0123456789")
    for i in a:
        if i[0] == '0':continue
        for j in range(7):
            if int(i[j+1:j+4])%t[j] != 0:
                break
        else:
            Sum += int(i)
    print Sum

if __name__ == '__main__':
    main()
