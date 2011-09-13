#!/usr/bin/env python
def main():
    sumList = [(1, 1)]
    n = 2
    while True:
        sumList.append((n, sumList[-1][1]+n))
        if sumList[-1][1] > 2000000:
            break
        n += 1
    result = None
    for i in range(len(sumList)):
        for j in range(i, len(sumList)):
            if sumList[i][0] <= sumList[j][0]:
                t = abs(sumList[i][1] * sumList[j][1] - 2000000)
                if not result:
                    result = t
                    a, b = sumList[i][0], sumList[j][0]
                elif t < result:
                    result = t
                    a, b = sumList[i][0], sumList[j][0]
    print a * b

if __name__ == '__main__':
    main()
