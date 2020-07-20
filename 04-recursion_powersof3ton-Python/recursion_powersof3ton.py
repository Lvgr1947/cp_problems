# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 
l = []
def powersOf3ToN(x):
	if x>1 and x%3 == 0:
		return powersOf3ToN(x//3)
	elif x == 1 :
		return True
	else:
		return False
def recursion_powersof3ton(n):
	n = int(n)
	if n>0:
		global l
		# print(powersOf3ToN(n))
		if powersOf3ToN(n):
			l.append(n)
		return recursion_powersof3ton(n-1)
	elif len(l)>0:
		sorted(l)
		return l
	else:
		return None
print(recursion_powersof3ton(0))
print(recursion_powersof3ton(42))
print(recursion_powersof3ton(0.45))
print(recursion_powersof3ton(1))
print(recursion_powersof3ton(3))
print(recursion_powersof3ton(8.99))
print(recursion_powersof3ton(9))
print(recursion_powersof3ton(1))
print(recursion_powersof3ton(1))
print(recursion_powersof3ton(1))