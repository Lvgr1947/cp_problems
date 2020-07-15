# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def sqares(n):
	sum = 0
	while(n > 0):
		x = n % 10
		sum += x*x
		n = n//10
	return sum

def ishappynumber(n):
	z = []
	if n == 1:
		return True
	elif(n > 1):
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
  

def fun_nth_happy_number(n):
	count = 0
	i = 0
	while(count!=n):
		while(True):
			if(ishappynumber(i)):
				break
			else:
				i += 1
		count += 1
	print(i)
	fun_nth_happy_number(7)