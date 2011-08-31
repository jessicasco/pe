#!/usr/bin/env python
import os

def main():
    datafile = os.path.abspath(__file__)[:-2] + 'txt'
    data = sorted(open(datafile).read().split(','))
    print sum(
            sum(ord(c)-ord('A')+1 for c in data[i] if c.isalpha()) * (i+1) 
            for i in range(len(data))
            )

if __name__ == '__main__':
    main()
