# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
s = 0
def onlyEvenDigits(L):
	global s
	print(L)
	if L > 0:
		r = L % 10
		if r % 2 == 0:
			s = s + r
		L = L//10
		if L == 0:
			# print(s)
			a=s
			s=0
			return a
		onlyEvenDigits(L)

	else:
		return 0
def fun_recursion_onlyevendigits(l):
	for i in range(len(l)):
		l[i] = onlyEvenDigits(l[i])
	return l
print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))