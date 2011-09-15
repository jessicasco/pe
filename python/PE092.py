#!/usr/bin/env python
def main():
    N = 10000000
    D = dict((str(i), i*i) for i in range(10))
    T = set()
    S = set()
    count = 0
    for i in range(1, N):
        j = i
        while True:
            if j == 89 or j in T:
                count += 1
                T.add(i)
                break
            elif j == 1 or j in S:
                S.add(i)
                break
            j = sum(D[c] for c in str(j))
    print count

if __name__ == '__main__':
    main()
