#!/usr/bin/env python
import math

def main():
    """Only need to calculate the max powers of the primes which are under the target."""
    primeList = [2, 3, 5, 7, 11, 13, 17, 19] 
    res = 1
    for prime in primeList:
        maxPower = int(math.floor(math.log(20, prime)))
        res *= pow(prime, maxPower)
    print res

if __name__ == '__main__':
    main()
