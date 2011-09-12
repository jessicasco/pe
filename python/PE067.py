#!/usr/bin/env python
def main():
    triangle = [
            [int(num) for num in line.split()]
            for line in open("PE067.txt")
            ]
    for i in range(len(triangle)-1,0,-1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
    print triangle[0][0]

if __name__ == '__main__':
    main()
