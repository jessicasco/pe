#!/usr/bin/env python

def prime4(n):
    count = 0
    if not n%2:
        count += 1
        while not n%2: 
            n /= 2
    t = 3
    while t**2 <= n:
        if not n%t:
            count += 1
            while not n%t:
                n /= t
        t += 2
    if n != 1:
        count += 1
    if count == 4:
        return True
    return False

def main():
    i = 1
    while True:
        if prime4(i) and prime4(i+1) and prime4(i+2) and prime4(i+3):
            break
        i += 1
    print i

if __name__ == '__main__':
    main()
