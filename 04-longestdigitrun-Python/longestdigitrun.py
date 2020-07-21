# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def lookandsay(a):
	c=1
	l = []
	for i in range(1,len(a)+1):
		if i<len(a) and a[i-1] == a[i]:
			c += 1
		else:
			l.append((c,a[i-1]))
			c = 1
	return(l)
def longestdigitrun(n):
	n = list(map(int,str(abs(n))))
	n = lookandsay(n)
	a = b = 0
	for i in n:
		if i[0] == a and i[1]< b: b = i[1]
		elif i[0]>a:a,b = i[0],i[1]
	return b
print(longestdigitrun(117773732))
print(longestdigitrun(-677886))
print(longestdigitrun(112233455567))
print(longestdigitrun(44332211))
print(longestdigitrun(4422113355))
print(longestdigitrun(12345))
print(longestdigitrun(123330001))