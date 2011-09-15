#!/usr/bin/env python
import itertools
def main():
    L = [str(i) for i in range(10)]
    squares = ["%02d" % (i*i) for i in range(1, 10)]
    print squares
    count = 0
    for a in itertools.combinations(L, 6):
        for b in itertools.combinations(L, 6):
            a = list(a)
            b = list(b)
            if ('6' in a) and ('9' not in a):
                a.append('9')
            if ('6' in b) and ('9' not in b):
                b.append('9')
            if ('9' in a) and ('6' not in a):
                a.append('6')
            if ('9' in b) and ('6' not in b):
                b.append('6')
            for square in squares:
                if (square[0] in a) and (square[1] in b):
                    continue
                elif (square[0] in b) and (square[1] in a):
                    continue
                break
            else:
                count += 1
    print count / 2

if __name__ == '__main__':
    main()
