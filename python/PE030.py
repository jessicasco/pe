#!/usr/bin/env python

"""
First, do a little math to estimate the range of the number: 
    I get to know that the numbers will not exceed 1000000
"""

pow5 = [i ** 5 for i in range(10)]

def fifthPower(n):
    global pow5
    return sum(map(lambda x: pow5[int(x)], str(n)))

def main():
    print sum(i for i in range(10, 1000000) if i == fifthPower(i))

if __name__ == '__main__':
    main()
