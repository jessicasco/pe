#!/usr/bin/env python
def factor(n):
    res = 1
    for i in range(n):
        res *= (i+1)
    return res

def main():
    print sum(map(int, str(factor(100))))

if __name__ == '__main__':
    main()
