#!/usr/bin/env python

"""
The Sieve of Eratosthenes:
    1. Make a list of all numbers from 2 to N
    2. Find the next number p not yet crossed out. This is a prime. 
        If it is greater than sqrt(N), go to 5.
    3. Cross out all multiples of p which are not yet crossed out.
    4. Go to 2.
    5. The numbers not crossed out are the primes not exceeding N.

Need to start crossing out multiples at p*p, 
because any smaller multiple of p has a prime divisor less than p 
and has already been crossed out as a multiple of that. 
This is also the reason why to stop after reaching sqrt(N)
"""

import math

"""
First version:
"""
"""
def getPrimeList(limit):
    crosslimit = int(math.sqrt(limit))
    sieve = [False] * (limit+2)
    for n in range(4, limit+1, 2):
        sieve[n] = True
    for n in range(3, crosslimit+1, 2):
        if not sieve[n]:
            for m in range(n*n, limit+1, 2*n):
                sieve[m] = True
    sieve = [i for i in range(2, limit+1) if not sieve[i]]
    return sieve
"""

"""
Second version:
    Only take into considerations the odd number, then add 2.
    Care about the index
"""
def getPrimeList(limit):
    sievebound = (limit-1) / 2
    sieve = [False] * (sievebound + 1)
    crosslimit = (int(math.sqrt(limit)) - 1) / 2
    for i in range(1, crosslimit+1):
        if not sieve[i]: # 2*i+1 is prime, mark multiples
            for j in range(2*i*(i+1), sievebound+1, 2*i+1):
                sieve[j] = True
    sieve = [ 2*i+1 for i in range(1, sievebound+1) if not sieve[i]]
    sieve.insert(0, 2)
    return sieve

def main():
    sieve = getPrimeList(2000000)
    print sum(sieve)

if __name__ == '__main__':
    main()
