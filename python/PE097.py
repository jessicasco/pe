#!/usr/bin/env python
def main():
    result = [0] * 10
    result[0] = 1
    power = 7830457
    for i in range(power):
        carry = 0
        for j in range(len(result)):
            carry += 2 * result[j]
            result[j] = carry%10
            carry /= 10
    print str(int("".join([str(i) for i in result][::-1])) * 28433 + 1)[-10:]

if __name__ == '__main__':
    main()
