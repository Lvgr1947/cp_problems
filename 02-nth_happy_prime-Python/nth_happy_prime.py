# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def sqares(n):
	sum = 0
	while(n > 0):
		x = n % 10
		sum += x*x
		n = n//10
	return sum

def ishappynumber(n):
	z = []
	if(n > 1):
		while(True):
			n = sqares(n)
			if(n == 1):
				return True	
			elif n in z:
				return False
			else:
				z.append(n)	
	else:
		return False
def isprime(n):
	if n>1:
		for i in range(2,n):
			if n%i == 0:
				return False
		else:
			return True

def fun_nth_happy_prime(n):
	count = 0
	i = 1
	if n == 0:
		# print(7)
		return 7
	elif n>0:
		while(count!=n+1):
			
			while(True):
				i += 1
				if(ishappynumber(i) and isprime(i)):
					break
			count += 1
		# print(i)
		return i