# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = [[m1[x][y]*m2[x][y] for y in range(len(m1[0]))] for x in range(len(m1))]
        return m3
    else:
        return None



