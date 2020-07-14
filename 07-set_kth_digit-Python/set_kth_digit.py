# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	fl
	n = str(n)
	n1 = list(n)
	if(len(n1)>k):
		n1[len(n1)-(k+1)] = str(d)
		n1 = ''.join(n1)
		return int(n1)
	else:
		n = str(d)+n
		return int(n)
# print(fun_set_kth_digit(123,2,5))