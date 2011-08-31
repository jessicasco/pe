#!/usr/bin/env python
import os

def main():
    datafile = os.path.abspath(__file__)[:-2] + 'txt'
    print str(sum(int(line) for line in open(datafile)))[0:10]

if __name__ == '__main__':
    main()
