# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

def strings(s4,s,j):
	a=""
	for i in range(len(s4)):
			if(i-j)):
				s += s4[i]
def fun_replace(s1, s2, s3):
	s4 = s1.split(s2)
	print(s4)
	if(len(s4[0])==len(s1)):
		return s1
	else:
		s=""
		if(len(s4[0]) == 0):
			i = 1
			s = strings(s4,s3,i)

		
		return s
print(fun_replace("rldhellrldowo23ufn348hf oincodnrld123", "rld", "     "))

