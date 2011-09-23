#!/usr/bin/env python
def isPalindromic(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def base2(n):
    res = ""
    while n != 0:
        res = str(n%2) + res
        n /= 2
    return int(res)

def main():
    s = 0
    # A number in base 2 must be odd to be a palindrome
    for i in range(1, 1000000, 2):
        if isPalindromic(i) and isPalindromic(base2(i)):
            s += i
    print s

if __name__ == '__main__':
    main()
