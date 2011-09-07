#!/usr/bin/env python
from PE010 import getPrimeList

def f(n):
    primeList = getPrimeList(n)
    subPrimeList = []
    length = 1
    tmpList = []
    for i in primeList:
        if len(str(i)) == length:
            tmpList.append(i)
        else:
            length += 1
            subPrimeList.append(tmpList)
            tmpList = [i]
    else:
        subPrimeList.append(tmpList)
    
    for subIndex in range(len(subPrimeList)):
        primeList = subPrimeList[subIndex]
        while len(primeList) >= 8:
            i = primeList[0]
            primeList.remove(i)
            strNum = str(i)
            for j in range(3):
                stro = str(j)
                tmpList = strNum.split(stro)
                length = len(tmpList)
                if length == 1:
                    continue
                for ii in range(2**(length-1)-1):
                    count = 1
                    count2 = 0
                    for k in range(j+1, 10):
                        strr = str(k)
                        rstr = ""
                        for jj in range(length-1):
                            if (((ii>>jj)&1) == 1):
                                rstr += (tmpList[jj]+stro)
                            else:
                                rstr += (tmpList[jj]+strr)
                        rnum = int(rstr + tmpList[-1])
                        if rnum not in primeList:
                            count2 += 1
                        else:
                            count += 1
                        if 10-8-j < count2:
                            break
                    if count == 8:
                        print i
                        return True
    return False

def main():
    n = 1000000
    while True:
        res = f(n)
        if res:
            return
        n *= 10

if __name__ == '__main__':
    main()
