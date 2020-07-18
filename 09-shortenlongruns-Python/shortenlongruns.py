# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your functio may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	# Your code goes here
	c = 1
	a=[]
	for i in range(0,len(L)):
		if c<k:
			a.append(L[i])
			# print(L[i])
			print(L[i],i)
		# print(len(L)-2)
		if i<len(L)-1 and L[i] == L[i+1]:
			c += 1
		else:
			c = 1
	print(a)
	return a
shortenlongruns([2, 3, 5, 5, 5, 3], 2)