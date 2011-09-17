#!/usr/bin/env python
import itertools

def main():
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    for perm in itertools.permutations("0123456789", 10):
        perm = "".join(perm)
        if perm[0] == '0':continue
        for i in range(7):
            if int(perm[i+1:i+4]) % primes[i] != 0:
                break
        else:
            total += int(perm)
    print total

if __name__ == '__main__':
    main()
