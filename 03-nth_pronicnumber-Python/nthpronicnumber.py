# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def ispronic(n):
	l = len(str(n))
	if l%2 == 0:
		l = l//2 + 1
	else:
		l = l//2
	print(l,"l")
	for j in range(0,10**l):
		print( (j+1)*j )
		if (j)*(j+1) == n:
			print(i,"j")
			return True
	return False
def nthpronicnumber(n):
	if n == 0: return 0
	i , j = 0 , 0
	while(i<n):
		j += 1
		if ispronic(j):
			i += 1
	return j
# print(nthpronicnumber(1))
print(ispronic(2))