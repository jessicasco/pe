#!/usr/bin/env python
from PE069 import getPhi
def main():
    res = getPhi(10000000)
    minimum = 100
    for i in range(len(res)):
        a = sorted(list(str(i+2)))
        b = sorted(list(str(res[i])))
        if a == b and (i+2)*1.0/res[i] < minimum:
            minimum = (i+2)*1.0/res[i]
            mini = i+2
    print mini

if __name__ == '__main__':
    main()
