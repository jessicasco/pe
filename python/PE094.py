#!/usr/bin/env python
"""
a^2 + b^2 = c^2 = (2*a + 1)^2
or 
a^2 + b^2 = c^2 = (2*a - 1)^2
So:
    (3*a+2)^2 - 3*(b^2) = 1
    or
    (3*a-2)^2 - 3*(b^2) = 1
"""
import pell
def main():
    result = 0
    for a, b in pell.pell(3):
        if a < 7:
            continue
        if 2*a+2 > 1000000000:
            break
        if (a+2) % 3 == 0:
            result += 2*a+2
        if 2*a-2 > 1000000000:
            break
        if (a-2) % 3 == 0:
            result += 2*a-2 
    print result

if __name__ == '__main__':
     main()
