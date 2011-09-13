#!/usr/bin/env python
def main():
    matrix = [[int(i) for i in line.split(",")] for line in open("PE081.txt")]
    N = 80
    nDict = {}
    for j in range(N):
        for i in range(N):
            minn = 0
            if j > 0:
                if i > 0:
                    minn = min(nDict[(i-1,j)], nDict[(i,j-1)])
                else:
                    minn = nDict[(i,j-1)]
            nDict[(i,j)] = minn + matrix[i][j]
    while True:
        flag = False
        for j in range(N):
            for i in range(N):
                minn = nDict[(i,j)]
                if i > 0:
                    minn = min(minn, nDict[(i-1,j)]+matrix[i][j])
                if i < N -1:
                    minn = min(minn, nDict[(i+1,j)]+matrix[i][j])
                if j > 0:
                    minn = min(minn, nDict[(i,j-1)]+matrix[i][j])
                if nDict[(i,j)] != minn:
                    flag = True
                    nDict[(i,j)] = minn
        if not flag:
            break
    print min(nDict[(i, N-1)] for i in range(N))

if __name__ == '__main__':
    main()
