# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')
def fun_rotatestrings(input, d):
	Lfirst = input[0 : d] 
	Lsecond = input[d:] 
	Rfirst = input[0 : len(input)- abs(d)] 
	Rsecond = input[len(input)- abs(d) : ] 
	s_new=""
	if d == 0:
		print("s")
		return input
	elif d > len(input):
		d = d - len(input)
		Lfirst = input[0 : d] 
		Lsecond = input[d:] 
		s_new = Lsecond+Lfirst
		print(s_new)
		return s_new

	elif d < 0:
		s_new = Rsecond+Rfirst
		return s_new
		
	else:
		print("n")
		s_new = Lsecond+Lfirst
		print(s_new)
		return s_new
