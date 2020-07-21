# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def lookandsay(a):
	c=1
	l = []
	for i in range(1,len(a)+1):
		if i<len(a) and a[i-1] == a[i]:
			c += 1
		else:
			l.append((c,a[i-1]))
			c = 1
	return(l)
def nthwithproperty309(n):
	l = lookandsay(list(str(n**5)))
