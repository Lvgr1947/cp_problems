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
# import numpy as np
def matrixadd(X, Y):
	p = len(X[0])
	q = len(X)
	o = len(Y[0])
	u = len(Y)
	result = [[0 for j in range(p)] for i in range(q)]
	flag = True
	if(len(X) == len(Y)):
		for i in range(len(X)):
			if len(X[i]) != len(Y[i]):
				flag = False
	else:
		flag = False
	if (flag):
		for i in range(q):
			for j in range(p):
				result[i][j] = X[i][j] + Y[i][j]	
		return result
	else:	
		return None
		