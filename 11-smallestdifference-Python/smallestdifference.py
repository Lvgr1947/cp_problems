# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	sort(a)

	b = min(a)
	print(b)
	c = a.index(b)
	m = a.index(max(a))
	a[c] = m
	d = min(a)
	print(d)
	return d-b
print(smallestdifference([1, -3, 71, 68, 17]))