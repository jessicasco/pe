#!/usr/bin/env python
def main():
    a = 1
    b = 1
    i = 3
    c = a + b
    while len(str(c)) < 1000:
        a = b
        b = c
        c = a + b
        i += 1
    print i

if __name__ == '__main__':
    main()
