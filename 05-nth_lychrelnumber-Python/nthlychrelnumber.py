# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def ispalindrome(n):
	if n == reverse(n):
		return True
	return False
def reverse(n):
	n = str(n)
	n = n[::-1]
	return int(n)
def islychrel(n):
	max_i = 20
	for i in range(max_i):
		n = n + reverse(n)
		if ispalindrome(n):
			return False
	return True
		
def nthlychrelnumbers(n):
	i , j = 0 , 0
	while(i<n):
		j += 1
		if j != 89 and islychrel(j):
			i += 1
	return j
print(nthlychrelnumbers(1))
# print(islychrel(89))