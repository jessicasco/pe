#!/usr/bin/ev python

def f(a, b):
    '''compute the sum of multiples of a below b'''
    n = (b - 1) / a # the number of multiples of a below b
    return a * (n * (n + 1) / 2)


def main():
    print f(3, 1000) + f(5, 1000) - f(3*5, 1000)

if __name__ == '__main__':
    main()
