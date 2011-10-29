#!/usr/bin/env python
import pell
def main():
    for tt, bb in pell.pell_k(2, -1, 2*120-1, 2*85-1):
        total = (tt+1)/2
        blue = (bb+1)/2
        if total > 1000000000000:
            break
    print blue

if __name__ == '__main__':
    main()
