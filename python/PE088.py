#!/usr/bin/env python
from math import sqrt
 
def unique(t):
    u = {}
    for x in t: u[tuple(x)] = 1
    return [list(x) for x in u.keys()]
 
class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, *args, **keywords):
        key = (args, tuple(keywords.items()))
        if key not in self.cache: 
            self.cache[key] = self.func(*args, **keywords)
        return self.cache[key]
 
@Memoize
def factorize_r(n, r): # r is number of factors
    if r==1: return [[n]]
    res=[]
    for f in xrange(2, int(sqrt(n)+1.0001)):
        if n%f==0:
            for j in factorize_r(n/f, r-1):
                res.append(sorted([f]+j))
    return unique(res)
 
def factorize(n):
    res, r = [], 1
    while True:
        t = factorize_r(n, r)
        if t==[]: return res
        res += t
        r += 1
 
mpsn = [999999]*12001
for n in xrange(4, 24001):
    for factors in factorize(n):
        if sum(factors) <= n:
            k = len(factors)+n-sum(factors)
            if k <= 12000 and n < mpsn[k]:
                mpsn[k] = n
 
print sum(set(mpsn[2:]))
