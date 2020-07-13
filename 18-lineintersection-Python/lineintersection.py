# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.
def fun_ismultiple(m, n):
	if(n<m):
		(m,n) = (n,m)
	if n!=0:
		if m%n==0:
			return True
		else:
			return False
def lineintersection(m1, b1, m2, b2):
	# your code goes here

	if (m1 != m2 and b1 != b2):
		if not (fun_ismultiple(m1,m2)): 
			return ((b1-b2)/(m2-m1))
		else:
			return None
	else:
		return None
  
  
