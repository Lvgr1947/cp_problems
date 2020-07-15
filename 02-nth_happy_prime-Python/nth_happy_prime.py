# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def squares(n):
	sum = 0
	while(n>0):
		x = n%10
		sum+=x*x
		n = n//10
	return sum
  
def ishappynumber(n):
	# your code goes here
	z = []
	if n>2:
		while(True):
			m = squares(n)
			if m == 1:
				return True
			elif m in z:
				return False
			else:
				z.append(m)
	else:
		return False

def prime(n):
	if n>1:
		for i in range(2,n):
			if n%i == 0:
				return False
		else:
			return True

def fun_nth_happy_prime(n):
	count = 0
	i = 1
	if n>=0:
		while(count<=n):
			while(True):
				i+=1
				if ishappynumber(i) and prime(i):
					break
			count+=1
		return i