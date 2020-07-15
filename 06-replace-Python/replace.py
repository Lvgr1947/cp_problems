# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	s4 = s1.split(s2)
	if(len(s4[0])==len(s1)):
		return s1
	else:
		s=""
		for i in range(len(s4)):
			if(len(s4[i]) == 0):
				print("fadf")
				s += s3
			else:
				s += s4[i]
		return s
print(fun_replace("hellrldowo23ufn348hf oincodnrld123", "rld", "     "))

