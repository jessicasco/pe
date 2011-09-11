#!/usr/bin/env python
import math
def limit(n):
    return math.exp((n-1)*1.0/n*math.log(10))

def main():
    count = 0
    i = 1
    while True:
        n = int(math.ceil(limit(i)))
        if n > 9:
            break
        count += 9 - n + 1
        i += 1
    print count

if __name__ == '__main__':
    main()
