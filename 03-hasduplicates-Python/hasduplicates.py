# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	list1 = []
	for i in range(len(L)):
		list1.extend(L[i])
	print(list1)
	if len(list1) != len(set(list1)):
		return True
	return False