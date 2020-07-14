# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(n, c):
	a=[]
	for i in range(n+1):
		a.append([])
		a[i].append(1)
		for j in range(1,i):
			a[i].append(a[i-1][j-1]+a[i-1][j])
		if(n!=0 and i!=0):
			a[i].append(1)
	b = a[n]
	if(len(b) >= c):
		return(b[c])
	else:
		print(0)
# fun_pascaltrianglevalue(1,1)