# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		else:
			return True


def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2
	c = 0
	i = 3
	while c!=n:
		x = str(i)
		y = x[::-1]
		print(x,y)
		if x == y:
			if isprime(i):
				c+=1
				print(i,c)
			if c == n:
				return i
		i+=1
	return False

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