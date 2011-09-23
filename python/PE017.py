#!/usr/bin/env python
def main():
    s = 0
    L = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    M = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for i in range(1, 1000):
        if i >= 100:
            s += len(L[i/100-1]) + len("hundred")
            if i%100 == 0:
                continue
            s += len("and")
            i %= 100
        if i >= 20:
            s += len(M[(i/10)-2])
            if i%10 == 0:
                continue
            i %= 10
        s += len(L[i-1])
    s += len("one") + len("thousand")
    print s

if __name__ == '__main__':
    main()
