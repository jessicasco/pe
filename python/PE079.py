#!/usr/bin/env python
def main():
    data = open("PE079.txt").read()
    digitList = [i for i in set(data) if i.isdigit()]
    numsList = data.split()
    beforeList=[]
    for d in digitList:
        digitBefore=[d]
        for num in numsList:
            if d in num:
                for j in range(num.index(d)):
                    digitBefore.append(num[j])
        beforeList.append(list(set(digitBefore)))
    resultList=[]
    while True:
        for b in beforeList:
            if len(b)==1:
                break
        resultList.append(b[0])
        beforeList.remove(b)
        length =len(beforeList)
        if length==0:
            break
        for i in range(length):
            beforeList[i].remove(b[0])
    print "".join(resultList)

if __name__ == '__main__':
    main()
