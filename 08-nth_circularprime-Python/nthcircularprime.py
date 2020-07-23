# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
l = []
def isprime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
          
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while i * i <= n : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
      
    return True
def checkCircular(N) : 
    count = 0
    temp = N 
    while (temp > 0) : 
        count = count + 1
        temp = temp / 10
          
    num = N; 
    while (isPrime(num)) : 
        rem = num % 10
        div = num / 10
        num = (int)((math.pow(10, count - 1))* rem)+ div 
        if (num == N) : 
            return True
      
    return False
def nthcircularprime(n):
	global l
	l = []
	m = []
	i , j = 1 , 1
	while(i < n):
		if checkCircular(j):
			# print( i, j , n)
			m.append((i,j))
			i += 1
		j += 1
	print(m)
	return j-1
# print(nthcircularprime(47))
print(isprime(131))
print(isprime(311))
print(isprime(113))
# print(iscircular(131))