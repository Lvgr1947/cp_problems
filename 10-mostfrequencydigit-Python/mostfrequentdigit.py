# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
		# your code goes here
	p=[]
	dicts = {}
	n = str(n)
	for i in n:
		if i in dicts:
			dicts[i] +=1
		else:
			dicts[i] = 0	

	a = max(dicts.values())
	for j in dicts.keys():
		if dicts[j] == a:
			p.append(int(j))	
	return min(p)		
		

		