#!/usr/bin/env python
def isPalindrome(n):
    if str(n)[::-1] == str(n):
        return True
    return False

def isLychrel(n):
    count = 49
    while count > 0:
        n += int(str(n)[::-1])
        if isPalindrome(n):
            return False
        count -= 1
    return True

def main():
    print sum(1 for i in range(10000) if isLychrel(i))

if __name__ == '__main__':
    main()
