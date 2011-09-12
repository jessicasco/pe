#!/usr/bin/env python
# coding=utf-8
"""
可以证明：
    每一个不是完全平方数的自然数N，其平方根可以写成简单连分数表示，
    并且其中a1,a2,..呈周期出现。 
"""
def getPeriod(n):
    num = int(n**0.5)
    if num*num == n:
        return 0
    fz = 1.0
    l = []
    length = 0
    while True:
        if (num*1.0, fz) in l:
            return length
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
