# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.
import numpy as np
def matrixadd(X, Y):
	p = len(X[0])
	q = len(X)
	o = len(Y[0])
	u = len(Y)
	print(p,q)

	result = np.zeros((q,p) , dtype = int)

	# print(len(X), len(Y))

	if ((q == u and p == o )):
		result= [ X[i][j] + Y[i][j] for j in range(len(X[0])) for i in range(len(X))]
		# print(result)	
		return result
	else:	
		return None	
