# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def istrue(x):
	L = [0,1,2,3,4,5,6,7,8,9]
	for i in range(len(L)):
		if str(L[i]) not in x:
			return False
	return True
def nthwithproperty309(n):
	i = -1
	j = 1
	while(i < n):
		if  istrue(str(n**5)):
			i += 1
	return

