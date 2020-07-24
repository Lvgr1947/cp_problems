# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	if n == 0: return 0
	i , j = 0 , 0
	while(i<n):
		j += 1
		if ispronic(j):
			i += 1
	return j 