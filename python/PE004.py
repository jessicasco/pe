#!/usr/bin/env python

def main():
    M = None
    a = 999
    while a >= 100:
        if a%11 == 0:
            step = 1
            b = a
        else:
            step = 11
            b = a / 11 * 11
        if M and a*b <= M:
            break
        while b >= 100:
            s = a * b
            if M and s <= M:
                break
            if str(s) == str(s)[::-1]:
                M = s
            b -= step
        a -= 1
    print M

if __name__ == '__main__':
    main()
