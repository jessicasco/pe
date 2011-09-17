#!/usr/bin/env python

def dynamic():
    """
    Dynamic Programming
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (200 + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, 200 + 1):
            ways[i] += ways[i-coin]
    print ways[200]

def recursive():
    """
    Recursive
    """
    L = [200, 100, 50, 20, 10, 5, 2, 1]

    def f(money, maxcoin):
        if maxcoin == 7:
            return 1
        s = 0
        for i in range(maxcoin, len(L)):
            if money - L[i] == 0:
                s += 1
            elif money - L[i] > 0:
                s += f(money - L[i], i)
        return s
    
    print f(200, 0)

def main():
    dynamic()
    # recursive()

if __name__ == '__main__':
    main()
