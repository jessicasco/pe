#!/usr/bin/env python

s = set(str(i) for i in range(1, 10))

def isPandigital(a, b):
    global s
    ss = str(a) + str(b) + str(a/b)
    if len(ss) == 9 and set(ss) == s:
        return True
    return False

def main():
    r = set()
    for a in range(1000, 10000):
        b = 2
        while b*b <= a:
            if a%b == 0 and isPandigital(a, b):
                r.add(a)
            b += 1
    print sum(r)

if __name__ == '__main__':
    main()
