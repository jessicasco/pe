#!/usr/bin/env python

def main():
    data = sorted(open("PE022.txt").read().split(','))
    print sum(
            sum(ord(c)-ord('A')+1 for c in data[i] if c.isalpha()) * (i+1) 
            for i in range(len(data))
            )

if __name__ == '__main__':
    main()
