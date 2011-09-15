#!/usr/bin/env python
def main():
    N = 50
    count = 0
    for x1 in range(N+1):
        for x2 in range(N+1):
            for y1 in range(N+1):
                for y2 in range(N+1):
                    if x1 == 0 and y1 == 0:
                        continue
                    if x2 == 0 and y2 == 0:
                        continue
                    if x1 == x2 and y1 == y2:
                        continue
                    if x1*x2 + y1*y2 == 0:
                        count += 1
                    elif (x2-x1)*x1 + (y2-y1)*y1 == 0:
                        count += 1
                    elif (x2-x1)*x2 + (y2-y1)*y2 == 0:
                        count += 1
    print count / 2

if __name__ == '__main__':
    main()
