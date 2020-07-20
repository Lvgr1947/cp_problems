# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		return True

def smithnumber(n):
    i = 2
    l = []
    j= 0
    print(n)
    while(n>1):
        print(n)
        if isprime(i):
            while(n%i == 0):
                print(n,i)
                l.append(i)
                n //= i
        i += 1
        j += 1
        if j == 10:
            break
    print(l)
    if 4==sum(l):
        return True

def fun_nth_smithnumber(n):
    smithnumber(n)
print(fun_nth_smithnumber(4))