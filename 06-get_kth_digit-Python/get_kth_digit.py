# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit = str(digit)
	digit = digit[::-1]
	digit = digit.split()
	print(len(digit))
	if(len(digit)>=k):
		return digit[k]
	else:
		return 0
    
print(fun_get_kth_digit(789,2))