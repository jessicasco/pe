#!/usr/bin/env python
D = {}
def f(num, maxnum):
    global D
    if (num, maxnum) in D:
        return D[(num, maxnum)]
    s = 0
    for i in range(1, maxnum+1):
        if num - i > 0:
            s += f(num - i, i)
        elif num - i == 0:
            s += 1
        else:
            break
    D[(num, maxnum)] = s
    return s

def main():
    print f(100, 99)

if __name__ == '__main__':
    main()
