#!/usr/bin/env python
def isLeap(n):
    if (n%4 == 0 and n%100 != 0) or n%400 == 0:
        return True
    return False

def main():
    day = [
            [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30], 
            [31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
            ]
    count = 0
    weekday = 1-31
    for i in range(1900, 2001):
        for j in range(12):
            weekday += day[isLeap(i)][j]
            weekday %= 7
            if weekday == 0 and i != 1900:
                count += 1
    print count

if __name__ == '__main__':
    main()
