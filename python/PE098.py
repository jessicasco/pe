#!/usr/bin/env python
import math
import itertools
def isSquare(n):
    s = int(math.sqrt(n))
    if s*s == n:
        return True
    else:
        return False

def main():
    words = [word[1:-1] for word in open("PE098.txt").read().split(',')]
    D = {}
    for word in words:
        if tuple(sorted(word)) not in D:
            D[tuple(sorted(word))] = [word]
        else:
            D[tuple(sorted(word))].append(word)
    for k, v in D.items():
        if len(v) == 1:
            D.pop(k)
    digits = [str(i) for i in range(10)]
    result = []
    for key, values in D.iteritems():
        key = list(set(key))
        for p in itertools.permutations(digits, len(key)):
            d = dict(map(None, key, p))
            numbers = []
            for v in values:
                n = "".join(d[c] for c in v)
                if not n.startswith('0') and isSquare(int(n)):
                    numbers.append(int(n))
            if len(numbers) >= 2:
                result.append(max(numbers))
    print max(result)

if __name__ == '__main__':
    main()
