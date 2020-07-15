# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	p = []
	q = {}
	n = str(n)
	for i in range(len(n)):
		if i not in q:
			q[i] = 0
		else:
			q[i] += 1
	a = max(q.values())
	for j in q.keys():
		if q[j] == a:
			p.append(j)