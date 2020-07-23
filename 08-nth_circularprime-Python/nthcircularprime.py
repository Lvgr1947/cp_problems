# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
l = []
def iscircular(n):
	global l
	if n not in l:
		if isprime(n):
			n = str(n)
			n = int(n[1:] + n[0]

			return iscircular()
def nthcircularprime(n):
	global l
	l = []
	i , j = 0 , 1
	while(j<n):
		if iscircular(n):
			i += 1
		j += 1
	return j