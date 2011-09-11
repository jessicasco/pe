#!/usr/bin/env python
def getPeriod(n):
    num = int(n**0.5)
    if num*num == n:
        return 0
    fz = 1.0
    l = []
    length = 0
    while True:
        if (num*1.0, fz) in l:
            return length - l.index((num*1.0, fz))
        else:
            l.append((num*1.0, fz))
            t = int(fz*(n**0.5 + num)/(n-num*num))
            fz = (n-num*num)/fz
            num = t*fz - num
            length += 1

def main():
    print sum(1 for i in range(2, 10001) if getPeriod(i)%2)

if __name__ == '__main__':
    main()
