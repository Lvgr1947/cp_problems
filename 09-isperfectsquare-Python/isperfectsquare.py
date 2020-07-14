# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	try:
		if(type(int(n))==int):
			print("true")
		elif(type(n) == int):
		
			i=2
			while(i<=math.sqrt(n)):
				if(i**2 == n):
					return True
				i += 1
			return False
	except:
		print(False)

isperfectsquare("hello")