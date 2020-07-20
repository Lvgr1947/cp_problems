# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 
l = []
def powersOf3ToN(x):
	if x>1 and x%3 == 0:
		powersOf3ToN(x//3)
	if x ==1 :
		True
def recursion_powersof3ton(n):
	n = int(n)
	global l
	if powersOf3ToN(n):
		l.append(n)
