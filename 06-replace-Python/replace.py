# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

def strings(s4,s,j):
	a=""
	for i in range(0,len(s4)):
		if i != len(s4)-1:
			a += s4[i]+ s
		else:
			a += s4[i]
	return a
    
def fun_replace(s1, s2, s3):
	s4 = s1.split(s2)
	if(len(s4[0])==len(s1)):
		return s1
	else:
		s=""
		i=0
		if(len(s4[0]) == 0):
			i = 1
			s += s3
		s = strings(s4,s3,i)
		return s
			

