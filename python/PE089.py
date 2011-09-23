#!/usr/bin/env python
D = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        }
N = dict((v, k) for k, v  in D.iteritems())
def getSum(s):
    global D
    total = 0
    i = 0
    while i < len(s):
        if (i < len(s)-1) and (s[i]+s[i+1] in D):
            total += D[s[i]+s[i+1]]
            i += 2
        else:
            total += D[s[i]]
            i += 1
    return total

def getMinimalForm(n):
    global N
    t = ''
    for i in sorted(N.keys(), reverse=True):
        t += n/i * N[i]
        n -= (n/i)*i
    return t

def main():
    saved = 0
    for s in open("PE089.txt"):
        total = getSum(s.strip())
        t = getMinimalForm(total)
        saved += len(s.strip()) - len(t)
    print saved

if __name__ == '__main__':
    main()
