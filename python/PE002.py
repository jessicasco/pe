#!/usr/bin/env python

def main():
    """
    odd, (even, odd, odd), (even, odd, odd), ...
    So slicing out every 3 number of the Fibonacci sequence results in the 
    sequence of all the even-valued terms in the Fibonacci sequence.
    f(n) = f(n-1) + f(n-2)
    f(n+6) = f(n+5) + f(n+4)
           = (f(n+4) + f(n+3)) + f(n+4)
           = 2*f(n+4) + f(n+3)
           = 2*(f(n+3) + f(n+2)) + f(n+3)
           = 3*f(n+3) + 2*f(n+2)
           = 3*f(n+3) + (f(n+2) + (f(n+1) + f(n)))
           = 3*f(n+3) + (f(n+2) + f(n+1)) + f(n)
           = 3*f(n+3) + f(n+3) + f(n)
           = 4*f(n+3) + f(n)
    The new sequence: 
    F(n+2) = 4*F(n+1) + F(n)
    with F(0) = 2, F(1) = 8
    """
    n = 4000000
    a = 2
    b = 8
    s = a + b
    c = 4 * b + a
    while c < n:
        s += c
        a = b
        b = c
        c = 4 * b + a
    print s

if __name__ == '__main__':
    main()
