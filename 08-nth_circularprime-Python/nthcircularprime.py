# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
l = []
def isprime(n):
	if n>1:
		for i in range(2,n//2+1):
			if n%i == 0 and i != n:
				return False
		return True
	return False
def iscircular(n):
	global l
	if n not in l:
		if isprime(n):
			l.append(n)
			print(n)
			n = str(n)
			if len(n) == 1:
				if isprime(int(n)): return True
			n = int(n[1:] + n[0])
			return iscircular(n)
		else:
			return False
	else:
		return True
def nthcircularprime(n):
	global l
	l = []
	m = []
	i , j = 1 , 1
	while(i < n):
		if iscircular(j):
			# print( i, j , n)
			m.append((i,j))
			i += 1
		j += 1
	print(m)
	return j-1
# print(nthcircularprime(47))
print(isprime(131))
print(isprime(311))
print(isprime(2))
# print(iscircular(131))