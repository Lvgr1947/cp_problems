# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	p = {}
	n = str(n)
	for i in n:
		if i not in p.keys():
			p[i] = 0
		else:
			p[i] += 