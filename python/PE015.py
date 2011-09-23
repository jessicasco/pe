#!/usr/bin/env python
def factor(n):
    res = 1
    while n != 1:
        res *= n
        n -= 1
    return res

def c(n,m):
    return (factor(n))/(factor(m)*factor(n-m))

def main():
    print c(20+20, 20)

if __name__ == '__main__':
    main()
