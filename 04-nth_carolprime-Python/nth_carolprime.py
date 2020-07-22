# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		else:
			return True

def fun_nth_carolprime(n):
    i = 2
    j = -1
    while(True):
        k = ((2**i - 1)**2 - 2)
        print(j,k, "out")
        if isprime(k) or ( (j+1)%3 == 0 and isprime(k//7)):
            print(k)
            j += 1
        # elif :
        #     print(k, "inside")
        #     j += 1
        if j == n: return k
        i += 1
fun_nth_carolprime(6)
# print(isprime(65023))
