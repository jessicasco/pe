#!/usr/bin/env python
import itertools
def main():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = []
    for t in itertools.permutations(s, 10):
        if t[1] < t[0] or t[2] < t[0] or t[3] < t[0] or t[4] < t[0]:
            continue
        b = t[0] + t[5] + t[6]
        for c in range(1,4):
            if t[c] + t[c+5] + t[c+6] != b:
                break
        else:
            if t[4] + t[9] + t[5] == b:
                res.append(t)
    result = []
    for x in res:
        s = ((str(x[0]) + str(x[5]) + str(x[6])) +
                (str(x[1]) + str(x[6]) + str(x[7])) +
                (str(x[2]) + str(x[7]) + str(x[8])) +
                (str(x[3]) + str(x[8]) + str(x[9])) +
                (str(x[4]) + str(x[9]) + str(x[5]))
                )
        if len(s) == 17:
            continue
        result.append(int(s))
    print max(result)

if __name__ == '__main__':
    main()
