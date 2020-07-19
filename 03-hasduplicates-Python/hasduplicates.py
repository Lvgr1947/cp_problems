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
# print(hasduplicates([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(hasduplicates([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(hasduplicates([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))
print(hasduplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(hasduplicates	([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))
print(hasduplicates([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 11]]))