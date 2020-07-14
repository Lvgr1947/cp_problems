# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	n = str(n)
	n1 = list(n)
	if(len(n1)>k):
		n1[len-k] = str(d)
		n1 = str(n1)
		return n1
	else:
		n = str(d)+n