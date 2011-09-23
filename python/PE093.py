#!/usr/bin/env python
import operator
import itertools
def getN(abcd):
    ops = [operator.add, operator.sub, operator.mul, operator.div]
    result = set()
    for a, b, c, d in itertools.permutations(abcd):
        a, b, c, d = a*1.0, b*1.0, c*1.0, d*1.0
        for e, f, g in itertools.product(ops, repeat=3):
            try:
                result.add(g(f(e(a, b), c), d)) # e, f, g
            except:
                pass
            try:
                result.add(f(e(a, b), g(c, d))) # e, g, f
            except:
                pass
            try:
                result.add(g(e(a, f(b, c)), d)) # f, e, g
            except:
                pass
            try:
                result.add(e(a, g(f(b, c), d))) # f, g, e
            except:
                pass
            try:
                result.add(f(e(a, b), g(c, d))) # g, e, f
            except:
                pass
            try:
                result.add(e(a, f(b, g(c, d)))) # g, f, e
            except:
                pass
    result = [int(a) for a in result if a == int(a)]
    i = 1
    while True:
        if i not in result:
            break
        i += 1
    return i - 1

def main():
    digits = [i for i in range(1, 10)]
    maxn = None
    for abcd in itertools.combinations(digits, 4):
        i = getN(abcd)
        if not maxn or i > maxn:
            maxn = i
            answer = abcd
    print "".join(str(i) for i in answer)

if __name__ == '__main__':
    main()
