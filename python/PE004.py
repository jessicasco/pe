#!/usr/bin/env python

def isPalindromic(n):
	n = str(n)
	if n == n[::-1]:
		return True
	else:
		return False

def main():
	"""
    First, we can show that the largest palindrome is a 6-digit number by the 
    fact that 111111 = 143 * 777. 
    Then xyzzyx = 100001*x + 10010*y + 1100*z = 11 * (9091*x + 910*y + 100*z). 
    So if xyzzyx = a * b, then either a or b should be divided by 11.
	By symmetry, we can assume a <= b.
	Let a and b decrease, we can break out in advance when their product is 
    too small compared to the current maxPalindrome
    """
	a = 999
	maxPalindrome = 0
	while a >= 100:
		if a % 11 == 0:
			step = 1
			b = 999
		else:
			step = 11
			b = 990
		if a * b < maxPalindrome:
			break
		while b >= a:
			if a * b < maxPalindrome:
				break
			if isPalindromic(a * b):
				maxPalindrome = a * b
			b -= step
		a -= 1
	print maxPalindrome

if __name__ == '__main__':
    main()
