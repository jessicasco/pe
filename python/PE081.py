#!/usr/bin/env python
def main():
    matrix = [[int(i) for i in line.split(",")] for line in open("PE081.txt")]
    N = 80
    nDict = {}
    for i in range(N):
        for j in range(N):
            minn = 0
            if j > 0:
                if i > 0:
                    minn = min(nDict[(i-1,j)], nDict[(i,j-1)])
                else:
                    minn = nDict[(i,j-1)]
            elif i > 0:
                minn = nDict[(i-1,j)]
            nDict[(i,j)] = minn + matrix[i][j]
    print nDict[(N-1, N-1)] 

if __name__ == '__main__':
    main()
