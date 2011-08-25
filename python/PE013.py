#!/usr/bin/env python

def main():
    print str(sum(int(line) for line in open("PE013.txt")))[0:10]

if __name__ == '__main__':
    main()
