#!/usr/bin/env python
S = set(str(i) for i in range(1, 10))
def isPandigital(a, b):
    global S
    s = str(a) + str(b) + str(a/b)
    if len(s) == 9 and set(s) == S:
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
