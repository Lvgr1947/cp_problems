# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2
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