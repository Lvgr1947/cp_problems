# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
def isauto(n):
	i = n*n
	while(n>0):
		if n%10 != i%10:
			return False
		n //= 10
		i //= 10
	return True
def nthautomorphicnumbers(n):
	i , j = 0 , -1
	while(i < n):
		j += 1
		if isauto(j):
			print("auto", j)
			i += 1
	return j
print(nthautomorphicnumbers(5))