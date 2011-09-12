#!/usr/bin/env python
# coding=utf-8
"""
这道题目的思想就是使用手工计算二次根的方法：
1．从个位起向左每隔两位为一节，若带有小数从小数点起向右每隔两位一节，
    用“，”号将各节分开； 
2．求不大于左边第一节数的平方根，为平方根最高上的数； 
3．从左边第一节数里减去求得的最高位上的数的平方，在它们的差的右边写上
    第二节数作为第一个余数； 
4．把商的最高位上的数乘20去试除第一个余数，所得的是整数作试商(如果这个
    最大整数大于或等于10，就用9或8作试商)； 
5．用最高位的数乘以20加上试商再乘以试商。如果所得的积小于或等于余数，
    这个试商就是平方根的第二位数；如果所得的积大于余数，就把试商逐次减小
    再试，直到积小于或等于余数为止； 
6．用同样的方法，继续求平方根的其他各位上的数。 
该方法的原理就是：(10a + b)2 = 100a2 + 20ab + b2
"""
def getSqrt(n):
    sqrtnum = int(n**0.5)
    remainder = n - sqrtnum**2
    if remainder == 0:
        return 0
    while True:
        remainder *= 100
        quotient = remainder / (20 * sqrtnum)
        if quotient >= 10:
            quotient = 9
        while quotient * (20 * sqrtnum + quotient) > remainder:
            quotient -= 1
        remainder -= quotient*(20 * sqrtnum + quotient)
        sqrtnum = sqrtnum * 10 + quotient
        if len(str(sqrtnum)) == 100:
            return sqrtnum

def getSum(n):
    return sum(int(i) for i in str(n))

def main():
    print sum(getSum(getSqrt(i)) for i in range(1, 101))

if __name__ == '__main__':
    main()
