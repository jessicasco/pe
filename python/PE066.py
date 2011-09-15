#!/usr/bin/env python
"""
pell equation:
    http://mathworld.wolfram.com/PellEquation.html
"""
def getX(n):
    num = int(n**0.5)
    fz = 1.0
    res = [num]
    l = []
    length = 0
    while True:
        if (num*1.0, fz) in l:
            break
        else:
            l.append((num*1.0, fz))
            t = int(fz*(n**0.5 + num)/(n-num*num))
            fz = (n-num*num)/fz
            num = t*fz - num
            length += 1
            res.append(t)
    if length % 2 == 0:
        length1 = length - 1
    else:
        for i in range(length):
            res.append(res[i+1])
        length1 = length*2 - 1
    p =[res[0], res[0]*res[1]+1]
    for i in range(length1):
        p.append(res[i+2]*p[-1] + p[-2])
    return p[length1]

def main():
    largest = 0
    index = 0
    for i in range(2, 1001):
        num = int(i**0.5)
        if num * num == i:
            continue
        x = getX(i)
        if x > largest:
            largest = x
            index = i
    print index

if __name__ == '__main__':
    main()
