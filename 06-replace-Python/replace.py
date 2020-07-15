# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	s4 = s1.split(s2)
	s = ""
	if len(s4[0]==0):
		s = s3+s4[1]
	elif len(s4[1]==0):
		s = s4[0]
	return s
# print(fun_replace("helloworld123", "hello", "345"))

