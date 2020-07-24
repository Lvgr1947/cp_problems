# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
def isauto(n):
	i = n*n
	f = str(i)
	d = len(str(n))
	if len(str(n)) == 1:
		s = i%10
		
		
		f = f[-1:-(d)]
		print(f)
	s = int(f)
	if s == n:
		return True
	return False
def nthautomorphicnumbers(n):
	i , j = 0 , -1
	while(i < n):
		j += 1
		if isauto(j):
			print("auto", j)
			i += 1
	return j
print(isauto(25))