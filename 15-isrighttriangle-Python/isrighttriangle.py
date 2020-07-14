# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

# import math

import math

def distance(x, y, a, b):
	dist = math.sqrt(((a-x)**2) + ((b-y)**2))
	return dist

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	A = distance(x1,y1,x2,y2)
	B = distance(x1,y1,x3,y3)
	C = distance(x2,y2,x3,y3)
	num = [A,B,C]
	x,y,z = sorted(num)
	if (x**2 + y**2 == z**2) or (y**2 + z**2 == x**2) or (z**2 + x**2 == y**2):
		return True
	else:
		return False
	m1 = int((y2-y1)/(x2-x1))
	



