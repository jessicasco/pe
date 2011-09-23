#!/usr/bin/env python
def SumOfSquares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6
    
def SquareOfSum(n):
    return (n * n * (n + 1) * (n + 1)) / 4

def main():
    print SquareOfSum(100) - SumOfSquares(100)

if __name__ == '__main__':
    main()
