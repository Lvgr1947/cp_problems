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
	l = a//2 + 1
	while(l>c and a >= c**2):
		# print(a,c)
		if isprime(c) and a%c == 0:
			if a%(c**2) != 0:
				return False
		c += 1
		if l-1 == c:
			return True
		
	return False
		
	
def nthpowerfulnumber(n):
	if n == 0:
		return 1
	i,j = 0,2
	while(i<n):
		if lookandsay(j):
			i += 1
		j += 1
	return j-1

# print(nthpowerfulnumber(1))
# print(nthpowerfulnumber(2))
# print(nthpowerfulnumber(3))
# print(nthpowerfulnumber(4))
# print(nthpowerfulnumber(5))
# print(nthpowerfulnumber(6))
# print(nthpowerfulnumber(7))
# print(nthpowerfulnumber(8))
# print(nthpowerfulnumber(9))
# print(nthpowerfulnumber(7))
# print(nthpowerfulnumber(8))
# print(nthpowerfulnumber(9))
# print(nthpowerfulnumber(10))
# print(nthpowerfulnumber(0))