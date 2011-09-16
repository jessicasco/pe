#!/usr/bin/env python
import math
def main():
    result = []
    for line in open("PE099.txt"):
        base, exp = line.strip().split(",")
        result.append(int(exp) * math.log(int(base)))
    print result.index(max(result)) + 1

if __name__ == '__main__':
    main()
