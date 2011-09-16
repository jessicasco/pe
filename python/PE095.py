#!/usr/bin/env python
# coding=utf-8
def main():
    N = 1000000
    properFactorSum = [1] * (N+1)
    i = 2
    while i*i <= N: # 因子对中的首项
        j = i +1
        while i*j <= N: # 因子对中的末项
            properFactorSum[i*j] += i+j
            j += 1
        i += 1
    i = 2
    while i*i <= N:
        properFactorSum[i*i] += i
        i += 1
    maxlen = 0
    for i in range(1, N+1):
        pt = properFactorSum[i]
        properFactorSum[i] = 1
        if pt == 1:
            continue
        chain = []
        while pt != 1 and pt <= N:
            chain.append(pt)
            pt = properFactorSum[pt]
            properFactorSum[chain[-1]] = 1
            if pt in chain:
                length = len(chain) - chain.index(pt)
                if length > maxlen:
                    maxlen = length
                    result = min(chain[chain.index(pt):])
    print result

if __name__ == '__main__':
    main()
