#!/usr/bin/env python

def main():
    """
    odd, (even, odd, odd,) even,....
    a, b, a+b, a+2b, 2a+3b, 3a+5b, 5a+8b, 8a+13b
    8a+13b = 4*(2a+3b) + 1*b
    from f(n+2) = f(n+1) + f(n)
    we can conclude:
    f(n+6) = 4*f(n+3) + 1*f(n)
    This is another seqence:
    g(n+2) = 4*f(n+1) + 1*f(n)
    """
    a = 2
    b = 8
    s = 2 + 8
    c = 4*b + a
    while c <= 4000000:
        s += c
        a = b
        b = c
        c = 4*b + a
    print s
if __name__ == '__main__':
    main()
