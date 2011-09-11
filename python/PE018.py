#!/usr/bin/env python
def main():
    """From bottom to up"""
    data = [map(int, line.split()) for line in open("PE018.txt")]
    for row in range(len(data)-1, 0, -1):
        for col in range(0, len(data[row])-1):
            data[row-1][col] += max(data[row][col], data[row][col+1])
    print data[0][0]

if __name__ == '__main__':
    main()
