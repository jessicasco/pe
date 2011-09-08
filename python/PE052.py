#!/usr/bin/env python

def main():
    i = 1
    while True:
        t = list(str(i))
        t.sort()
        for j in range(2, 7):
            k = list(str(i*j))
            k.sort()
            if t != k:
                break
        else:
            print i
            break
        i += 1

if __name__ == '__main__':
    main()
