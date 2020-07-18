# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
def fun_nth_additive_prime(n):
	if n == 0:
		return 2
	c = 0
	i = 3
	while c!=n:		
		if isprime(i):
			sum=0
			temp = str(i)
			for x in temp:
				sum+=int(x)
			if isprime(sum):
				c+=1
			if c == n:
				return i
		i+=1
	return False