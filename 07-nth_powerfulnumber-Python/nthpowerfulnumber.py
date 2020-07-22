# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		else:
			return True
def lookandsay(a):
	c=2
	l = []
	while(a>0):
		if isprime(c):
			j=0
			while(a%c == 0) and j<2:
				j += 1
				l.append(j)
				a //= c
			if j==1:
				return False
		c += 1
	return True
		
	
def nthpowerfulnumber(n):
	if n == 0:
		return 1
	i,j = 0,2
	while(i<n):
		if lookandsay(j):
			i += 1
		j += 1
	return j