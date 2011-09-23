#!/usr/bin/env python
from PE007 import isPrime
def main():
    i = 9876543
    while True:
        if isPrime(i):
            if set(str(i)) == set(str(j+1) for j in range(len(str(i)))):
                print i
                return 
        i -= 2

if __name__ == '__main__':
    main()
