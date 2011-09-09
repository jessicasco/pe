#!/usr/bin/env python

"""
High Card = 0
One Pair = 1
Two Pairs = 2
Three of a Kind = 3
Straight = 4
Flush = 5
Full House = 6
Four of a Kind = 7
Straight Flush = 8
Royal Flush = 9
"""

def f1(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            t = s[i:i+2]
            a = s[i+2:]
            a.reverse()
            t += a
            a = s[:i]
            a.reverse()
            t += a
            return t

def f2(s):
    if s[0] == s[1] and s[2] == s[3]:
        return s[2:4] + s[0:2] + s[4]
    if s[0] == s[1] and s[3] == s[4]:
        return s[3:5] + s[0:2] + s[2]
    return s[3:5] + s[1:3] + s[0]

def f3(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            t = s[i:i+3] 
            a = s[i+3:]
            a.reverse()
            t += a
            a = s[:i]
            a.reverse()
            t += a
            return t

def value(s):
    m = []
    for i in s:
        if i[0] == 'T':
            m.append(10)
        elif i[0] == 'J':
            m.append(11)
        elif i[0] == 'Q':
            m.append(12)
        elif i[0] == 'K':
            m.append(13)
        elif i[0] == 'A':
            m.append(14)
        else:
            m.append(int(i[0]))
    m.sort()
    return m

def isOnePair(s):
    s.sort()
    for i in range(len(s)-1):
        if s[i][0] == s[i+1][0]:
            return True
    return False

def isTwoPairs(s):
    s.sort()
    if s[0][0] == s[1][0] and s[1][0] != s[2][0] and s[2][0] == s[3][0]:
        return True
    if s[0][0] == s[1][0] and s[1][0] != s[3][0] and s[3][0] == s[4][0]:
        return True
    if s[1][0] == s[2][0] and s[2][0] != s[3][0] and s[3][0] == s[4][0]:
        return True
    return False

def isThreeOfAKind(s):
    s.sort()
    if s[0][0] == s[2][0] or s[1][0] == s[3][0] or s[2][0] == s[4][0]:
        return True
    return False

def isFullHouse(s):
    s.sort()
    if s[0][0] == s[2][0] and s[3][0] == s[4][0]:
        return True
    if s[0][0] == s[1][0] and s[2][0] == s[4][0]:
        return True
    return False

def isFourOfAKind(s):
    s.sort()
    if s[0][0] == s[3][0] or s[1][0] == s[4][0]:
        return True
    return False

def isStraight(s):
    m = []
    for i in s:
        if i[0] == 'T':
            m.append(10)
        elif i[0] == 'J':
            m.append(11)
        elif i[0] == 'Q':
            m.append(12)
        elif i[0] == 'K':
            m.append(13)
        elif i[0] == 'A':
            m.append(14)
        else:
            m.append(int(i[0]))
    m.sort()
    for i in range(4):
        if (m[i] + 1) != m[i+1]:
            return False
            break
    else:
        return True

def rank(s):
    result = 0
    isFlush = False
    for i in range(4):
        if s[i][1] != s[4][1]:
            break
    else:
        isFlush = True
        result = 5
    if isFlush:
        if isStraight(s):
            result = 8
            s.sort()
            if s[0][0] == 'A':
                result = 9
    elif isStraight(s):
        result = 4
    elif isOnePair(s):
        result = 1
        if isTwoPairs(s):
            result = 2
        if isThreeOfAKind(s):
            result = 3
            if isFullHouse(s):
                result = 6
            if isFourOfAKind(s):
                result = 7
    return result

def main():
    count = 0
    for line in open("PE054.txt"):
        line = line.split()
        a = line[:5]
        b = line[5:]
        if rank(a) > rank(b):
            count += 1
            continue
        elif rank(a) < rank(b):
            continue
        aa = value(a)
        bb = value(b)
        if aa == bb:
            continue
        if rank(a) == 0:
            aa.reverse()
            bb.reverse()
            if aa > bb:
                count += 1
        elif rank(a) == 1:
            aa = f1(aa)
            bb = f1(bb)
            if aa > bb:
                count += 1
        elif rank(a) == 2:
            aa = f2(aa)
            bb = f2(bb)
            if aa > bb:
                count += 1
        elif rank(a) == 3:
            aa = f3(aa)
            bb = f3(bb)
            if aa > bb:
                count += 1
        elif rank(a) == 4:
            if aa[0] > bb[0]:
                count += 1
        elif rank(a) == 5:
            aa.reverse()
            bb.reverse()
            if aa > bb:
                count += 1
        elif rank(a) == 6:
            if aa[1] != aa[2] and bb[1] != bb[2]:
                if aa[2] > bb[2]:
                    count += 1
                elif aa[2] == bb[2] and aa[0] > bb[0]:
                    count += 1
            elif aa[1] != aa[2] and bb[1] == bb[2]:
                if aa[2] > bb[2]:
                    count += 1
            elif aa[1] == aa[2] and bb[1] != bb[2]:
                if aa[2] > bb[2]:
                    count += 1
                elif aa[2] == bb[2]:
                    count += 1
            elif aa[1] == aa[2] and bb[1] == bb[2]:
                if aa[2] > bb[2]:
                    count += 1
                elif aa[2] == bb[2] and aa[4] > bb[4]:
                        count += 1
        elif rank(a) == 7:
            if aa[0] != aa[1] and bb[0] != bb[1]:
                if aa[1] > bb[1]:
                    count += 1
                elif aa[1] == bb[1] and aa[0] > bb[0]:
                    count += 1
            elif aa[0] != aa[1] and bb[0] == bb[1]:
                if aa[1] > bb[1]:
                    count += 1
            elif aa[0] == aa[1] and bb[0] != bb[1]:
                if aa[1] > bb[1]:
                    count += 1
                elif aa[1] == bb[1]:
                    count += 1
            if aa[0] == aa[1] and bb[0] == bb[1]:
                if aa[1] > bb[1]:
                    count += 1
                elif aa[1] == bb[1] and aa[4] > bb[4]:
                    count += 1
        elif rank(a) == 8:
            if aa[0] > bb[0]:
                count += 1
        elif rank(a) == 9:
            pass
    print count

if __name__ == '__main__':
    main()
